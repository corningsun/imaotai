ITEM_MAP = {
    # 2024
    "10941": "53%vol 500ml贵州茅台酒（甲辰龙年）",
    "10942": "53%vol 375ml×2贵州茅台酒（甲辰龙年）",
    # 2023 已下架
    "10213": "53%vol 500ml贵州茅台酒（癸卯兔年）",
    "10214": "53%vol 375ml×2贵州茅台酒（癸卯兔年）",
    # 一直有
    "2478": "53%vol 500ml贵州茅台酒（珍品）",
    "10056": "53%vol 500ml茅台1935",
}

# 需要预约的商品(默认只预约2个兔茅)
########################
ITEM_CODES = ['10941', '10942']



########################
# 推送消息，可以不填
PUSH_TOKEN = None

# 飞书群机器人
#PUSH_TOKEN = 'FeiShu'
PUSH_FEISHU_URL = 'https://open.feishu.cn/open-apis/bot/v2/hook/xxx-your-self-url'
########################

# credentials 路径，例如：CREDENTIALS_PATH = /home/user/.imoutai/credentials
# 不配置，使用默认路径，在宿主目录
# 例如： CREDENTIALS_PATH = '/home/user/.imautai/credentials'
########################
CREDENTIALS_PATH = '/home/user/.imautai/credentials'
########################

# 预约规则配置
########################
# 预约本市出货量最大的门店
MAX_ENABLED = False
# 预约你的位置附近门店
DISTANCE_ENABLED = True
########################

# 高德开放平台密钥：https://console.amap.com/dev/key/app
AMAP_KEY = '770ba0101e3501fb9b3ef332d3d79723'
