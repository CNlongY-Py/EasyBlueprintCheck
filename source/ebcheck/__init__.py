import nbtlib
import os
default_cfg={
    "blacklist":[
        "creative",
        "create:handheld_worldshaper",
        "shulker_box",
        "command_block",
        "bedrock",
        "barrier",
        "structure_block",
        "debug_stick",
        "spawn_egg",
        "spawner"
    ],
    "kick_reason":"§c§n因为违规操作,您已经被此服务器封禁§r",
    "ban_reason":"§c§n使用作弊蓝图§r"
}
def on_load(server,old):
    global cfg
    server.logger.info("                                     ")
    server.logger.info("      ▓█████  ▄▄▄▄    ▄████▄         ")
    server.logger.info("      ▓█   ▀ ▓█████▄ ▒██▀ ▀█         ")
    server.logger.info("      ▒███   ▒██▒ ▄██▒▓█    ▄        ")
    server.logger.info("      ▒▓█  ▄ ▒██░█▀  ▒▓▓▄ ▄██▒       ")
    server.logger.info("      ░▒████▒░▓█  ▀█▓▒ ▓███▀ ░       ")
    server.logger.info("      ░░ ▒░ ░░▒▓███▀▒░ ░▒ ▒  ░       ")
    server.logger.info("      ░ ░  ░▒░▒   ░   ░  ▒           ")
    server.logger.info("      ░    ░    ░ ░                  ")
    server.logger.info("      ░  ░ ░      ░ ░                ")
    server.logger.info("      ░ ░                            ")
    server.logger.info(" Powered By CNlongY-Py & YogurtCloud ")
    cfg=server.load_config_simple('config.json', default_cfg)
def on_info(server,info):
    if info.content[:23]=="New Schematic Uploaded:":
        spath=info.content[24:]
        player=spath.split("/")[0]
        blueprint=spath.split("/")[1]
        server.logger.info(f"检测到 {player} 上传了新的蓝图({blueprint})")
        sch = str(nbtlib.load(f"server/schematics/uploaded/{spath}"))
        for i in cfg["blacklist"]:
            if sch.find(i):
                server.logger.warning(f"检测到蓝图({spath})中含有({i})")
                server.execute(f"/kick {player} {cfg['kick_reason']}")
                server.execute(f"/ban {player} {cfg['ban_reason']}")
                server.logger.warning(f"已封禁玩家({player})")
                if not player in os.listdir("server/schematics/banned/"):
                    os.mkdir(f"server/schematics/banned/{player}")
                os.replace(f"server/schematics/uploaded/{spath}",f"server/schematics/banned/{spath}")
                server.logger.warning(f"作弊蓝图已被上传至(schematics/banned/{spath})")
                break