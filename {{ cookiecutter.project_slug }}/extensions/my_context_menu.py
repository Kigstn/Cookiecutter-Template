from core.base import CustomClient

from interactions import CommandType, ContextMenuContext, Message, context_menu, Extension


class ContextMenuExtension(Extension):
    bot: CustomClient

    @context_menu(name="repeat", context_type=CommandType.MESSAGE)
    async def my_context_menu(self, ctx: ContextMenuContext):
        """Repeat the message on which the context menu was used"""

        message: Message = ctx.target
        await ctx.send(message.content)


def setup(bot: CustomClient):
    """Let interactions load the extension"""

    ContextMenuExtension(bot)
