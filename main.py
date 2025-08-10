# main.py
import logging
from dotenv import load_dotenv
from livekit.agents.metrics import LLMMetrics, STTMetrics, TTSMetrics, EOUMetrics
import asyncio
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions, get_job_context
from livekit.plugins import (
    google,
    cartesia,
    deepgram,
    noise_cancellation,
    silero,
)
from livekit.plugins.turn_detector.multilingual import MultilingualModel

# Import your async tools (they already have @function_tool())
from tools import get_weather, search_web, send_email

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions="You are a helpful voice AI assistant named Bai.",
            # Pass the function_tool-decorated callables directly (no need for FunctionTool wrapper)
            tools=[get_weather, search_web, send_email],
        )

    async def on_start(self, ctx):
        # Called when the agent session starts; greet the user using session.say
        try:
            await ctx.session.say("Hello! I'm Bai — your voice assistant. I can check the weather, search the web, or send emails. How can I help you today?")
        except Exception:
            logger.exception("Failed to send startup greeting.")


async def entrypoint(ctx: agents.JobContext):
    """
    Entrypoint that starts the AgentSession for the current LiveKit job context.
    """
    session = AgentSession(
        stt=deepgram.STT(model="nova-3", language="multi"),
        llm=google.LLM(model="models/gemini-2.5-flash-lite"),  # update as needed
        tts=cartesia.TTS(model="sonic-2", voice="f786b574-daa5-4673-aa0c-cbe3e8534c02"),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )
    
    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            # LiveKit Cloud enhanced noise cancellation
            # - If self-hosting, omit this parameter
            # - For telephony applications, use `BVCTelephony` for best results
            noise_cancellation=noise_cancellation.BVC(), 
        ),
    )

    # Optionally generate a first reply if you want the LLM to produce an initial response
    await session.generate_reply(instructions="Offer help to the user in one sentence.")


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
