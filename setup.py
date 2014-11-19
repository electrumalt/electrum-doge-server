from setuptools import setup

setup(
    name="electrum-ixc-server",
    version="0.9",
    scripts=['run_electrum_ixc_server','electrum-ixc-server'],
    install_requires=['plyvel','jsonrpclib', 'irc'],
    package_dir={
        'electrumixcserver':'src'
        },
    py_modules=[
        'electrumixcserver.__init__',
        'electrumixcserver.utils',
        'electrumixcserver.storage',
        'electrumixcserver.deserialize',
        'electrumixcserver.networks',
        'electrumixcserver.blockchain_processor',
        'electrumixcserver.server_processor',
        'electrumixcserver.processor',
        'electrumixcserver.version',
        'electrumixcserver.ircthread',
        'electrumixcserver.stratum_tcp',
        'electrumixcserver.stratum_http'
    ],
    description="Ixcoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/ixcoin123/electrum-server/",
    long_description="""Server for the Electrum Lightweight Ixcoin Wallet"""
)


