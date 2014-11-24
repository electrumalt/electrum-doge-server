from setuptools import setup

setup(
    name="electrum-doge-server",
    version="0.9",
    scripts=['run_electrum_doge','electrum-doge-server'],
    install_requires=['plyvel','jsonrpclib', 'irc'],
    package_dir={
        'electrumdoge':'src'
        },
    py_modules=[
        'electrumdoge.__init__',
        'electrumdoge.utils',
        'electrumdoge.storage',
        'electrumdoge.deserialize',
        'electrumdoge.networks',
        'electrumdoge.blockchain_processor',
        'electrumdoge.server_processor',
        'electrumdoge.processor',
        'electrumdoge.version',
        'electrumdoge.ircthread',
        'electrumdoge.stratum_tcp',
        'electrumdoge.stratum_http'
    ],
    description="Doge Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/electrumalt/electrum-doge-server/",
    long_description="""Server for the Electrum Lightweight Dogecoin Wallet"""
)


