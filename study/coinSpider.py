import requests, io, sys
from lxml import etree

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'gb18030') 
''' 币安
headers = {
'cookie':'JSESSIONID=FAD62A87FCEFDB2DAE3DD8A362905B99; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216615909bb8110-055f28c7b34c9e-9393265-2073600-16615909bb9442%22%2C%22%24device_id%22%3A%2216615909bb8110-055f28c7b34c9e-9393265-2073600-16615909bb9442%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D; s9r1=5840F4D64BA5B647298C118DE5D46A22; p20t=web.10019218.EA4E15F9E327F9C174C7229B5D13CD8A; cr00=449B2A4EA25E0CDB0CB882F5DCDA5107; d1og=web.10019218.7CC2E18F4E8F608C8A8B2299BBBF09F0; r2o1=web.10019218.8049A5836C40FFA62803140D95A6AE68; f30l=web.10019218.348AEE21BAB8A5A32C8C650990A6093B; logined=y; CSRFToken=449B2A4EA25E0CDB0CB882F5DCDA5107; __BINANCE_USER_DEVICE_ID__={"420f7891ca372bb9e684f2002728a81b":{"date":1537960241174,"value":"1537960242423kwypUpq3vLig9vkd9eS"},"288966b1f116d006f28bcbff83010e3c":{"date":1533219501581,"value":"15332195019252bCBaVZCFUCnIf9F5ry"}}; lang=EN',
'referer':'https://www.binance.com/userCenter/balances.html',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'	
}

url = 'https://www.binance.com/en'
reponse = requests.get(url, headers = headers).text
s = etree.HTML(reponse)
binance_btc = s.xpath('//*[@id="__next"]/div/main/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div/a[2]/div[3]/text()')
#binance_btc_ = ['Ripple', 'Ethereum', 'Stellar Lumens', 'EOS', 'OST', 'Cardano', 'Bitcoin Cash', 'Litecoin', 'NANO', 'TRON', 'Agrello', 'Po.et', '0x', 'Binance Coin', 'NEO', 'Viberate', 'MIOTA', 'Ethereum Classic', 'IOStoken', 'TrueUSD', 'Monero', 'VIBE', 'VeChain', 'Ontology', 'QuarkChain', 'ICON', 'Dash', 'Zcash', 'Time New Bank', 'Lunyr', 'Siacoin', 'Storm', 'Request Network', 'AdEx', 'Metal', 'Mainframe', 'Zilliqa', 'Selfkey', 'Gifto', 'Qtum', 'Basic Attention Token', 'NEM', 'Pundi X', 'Genesis Vision', 'DOCK', 'Civic', 'AION', 'Nuls', 'Nucleus Vision', 'Verge', 'WaBi', 'Holo', 'Ripio Credit Network', 'openANX', 'CloakCoin', 'ChainLink', 'Bitcoin Diamond', 'Status', 'CyberMiles', 'Aeron', 'ETHOS', 'Wancoin', 'SingularDTV', 'aelf', 'Loom Network', 'Enigma', 'Walton', 'EnjinCoin', 'Etherparty', 'OmiseGO', 'Tierion', 'ChatCoin', 'Stratis', 'Steem', 'Waves', 'FunFair', 'Blox', 'GoChain', 'Bitcoin Gold', 'Cindicator', 'NAV Coin', 'Quantstamp', 'DENT', 'district0x', 'Monetha', 'Augur', 'Bytecoin', 'BlockMason Credit Protocol', 'Nexus', 'INS Ecosystem', 'Lisk', 'Streamr DATAcoin', 'MCO', 'EthLend', 'Populous', 'Theta Token', 'Aeternity', 'YOYOW', 'Ardor', 'IoTeX', 'AppCoins', 'ZCoin', 'AirSwap', 'Decentraland', 'BitShares', 'Modum', 'Triggers', 'Salt', 'Nebulas', 'GXChain', 'Red Pulse Phoenix', 'Bluzelle', 'POA Network', 'WePower', 'Komodo', 'Viacoin', 'Bread', 'SingularityNET', 'WINGS', 'Golem', 'PowerLedger', 'QLC Chain', 'Ark', 'Substratum', 'Neblio', 'Eidoo', 'NeoGas', 'Horizen', 'Groestlcoin', 'Loopring', 'Syscoin', 'Ambrosus', 'Storj', 'Polymath', 'Moeda Loyalty Points', 'Everex', 'KyberNetwork', 'iExecRLC', 'DigixDAO', 'Bancor', 'HyperCash', 'PIVX', 'SONM', 'Raiden Network Token', 'Skycoin', 'ICONOMI']
#binance_eth = s.xpath('//*[@id="__next"]/div/main/div[3]/div/div[2]/div/div[@class="s62mpio-0-sc-tilXH gFhkEW"]/div/div[2]/div/div[2]/a/a/div[3]') #分标签抓取不到内容

print(binance_eth)
'''
headers = {
'cookie':'__cfduid=dd5a283726fe6a499dcb88bee556c70f21537970973; HBP_inviterId=11292560; gr_user_id=6c0fcee0-1892-497a-bc50-fd58ca76ec5a; grwng_uid=f0f5bf33-a86b-42aa-a6ee-2ce6d456f0c1; SESSION=f3332115-93e5-4055-8b48-054ef98debe4; _ga=GA1.2.1767264370.1537973346; _gid=GA1.2.533955396.1537973346; __zlcmid=oahfgg0P4k4AVk; ADRUM=s=1537973665840&r=https%3A%2F%2Fwww.hbg.com%2Fzh-cn%2F%3F0',
'referer':'https://www.hbg.com/zh-cn/btc_usdt/exchange/',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'	
}

url = 'https://www.hbg.com/zh-cn/btc_usdt/exchange/'# 动态加载的数据如何获取
reponse = requests.get(url, headers = headers).text
s = etree.HTML(reponse)
huobi_usdt = s.xpath('//*[@id="head_nav"]/li[3]/a')

print(huobi_usdt)