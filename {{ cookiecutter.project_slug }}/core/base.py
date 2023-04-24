import os

from interactions import Client, listen


class CustomClient(Client):
    """Subclass of interactions.Client with on_startup event"""

    @listen()
    async def on_startup(self):
        """Gets triggered on startup"""

        self.logger.info(f"{os.getenv('PROJECT_NAME')} - Startup Finished!")
