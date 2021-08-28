discord.py with SlashCommands
==========

A modern, easy to use, feature-rich, and async ready API wrapper for Discord written in Python, supporting discord's interactions.


Key Features
-------------

- Modern Pythonic API using ``async`` and ``await``.
- Proper rate limit handling.
- Optimised in both speed and memory.

Installing
----------

**Python 3.8 or higher is required**

To install the library without full voice support, you can just run the following command:

.. code:: sh

    pip install git+https://github.com/Miolus/discord.py-SlashCommands


Optional Packages
~~~~~~~~~~~~~~~~~~

* `PyNaCl <https://pypi.org/project/PyNaCl/>`__ (for voice support)

Please note that on Linux installing voice you must install the following packages via your favourite package manager (e.g. ``apt``, ``dnf``, etc) before running the above commands:

* libffi-dev (or ``libffi-devel`` on some systems)
* python-dev (e.g. ``python3.6-dev`` for Python 3.6)

SlashCommand Example
--------------

.. code:: py

    import discord

    client = discord.Client()

    @client.command(name="ping", description="Ping me!")
    async def ping(ctx):
        await ctx.send("Pong!")

Bot Example
~~~~~~~~~~~~~

.. code:: py

    import discord
    from discord.ext import commands

    bot = commands.Bot(command_prefix='>')

    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    bot.run('token')

You can find more examples in the examples directory.


SlashCommand Context Object:

.. code:: py

    ctx.interaction -> discord.Interaction
    ctx.command -> discord.commands.ApplicationCommandCallback
    ctx.send -> Interaction.response.send_message
