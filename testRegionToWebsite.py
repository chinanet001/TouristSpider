import os
import platform
from apscheduler.schedulers.blocking import BlockingScheduler
region_to_websites_ubuntu = {
    '千岛湖':{
        '携程':'千岛湖',
        '马蜂窝': '千岛湖',
        '驴妈妈': '千岛湖',
        '飞猪': '千岛湖',

    },
    '西湖': {
        '携程': '西湖',
        '马蜂窝': '杭州西湖',
        '驴妈妈': '西湖',
        '飞猪': '西湖',

    },
    '西溪': {
        '携程': '西溪',
        '马蜂窝': '杭州西溪',
        '驴妈妈': '西溪',
        '飞猪': '西溪',

    },
    '溪口': {
        '携程': '溪口',
        '马蜂窝': '宁波溪口',
        '驴妈妈': '溪口',
        '飞猪': '溪口',

    },
    '乌镇': {
        '携程': '乌镇',
        '马蜂窝': '乌镇',
        '驴妈妈': '乌镇',
        '飞猪': '乌镇',

    },
    '西塘': {
        '携程': '西塘',
        '马蜂窝': '西塘',
        '驴妈妈': '西塘',
        '飞猪': '西塘',

    },
    '横店': {
        '携程': '横店',
        '马蜂窝': '横店',
        '驴妈妈': '横店',
        '飞猪': '横店',

    },
    '江郎山': {
        '携程': '江郎山',
        '马蜂窝': '江郎山',
        '驴妈妈': '江郎山',
        '飞猪': '江郎山',

    },
    '雁荡山': {
        '携程': '雁荡山',
        '马蜂窝': '雁荡山',
        '驴妈妈': '雁荡山',
        '飞猪': '雁荡山',

    },
    '普陀山': {
        '携程': '普陀山',
        '马蜂窝': '普陀山',
        '驴妈妈': '普陀山',
        '飞猪': '普陀山',

    },
    '南浔': {
        '携程': '南浔古镇',
        '马蜂窝': '南浔',
        '驴妈妈': '南浔古镇',
        '飞猪': '南浔',

    },
    '神仙居': {
        '携程': '神仙居',
        '马蜂窝': '神仙居',
        '驴妈妈': '神仙居',
        '飞猪': '神仙居',

    },
    '天台山': {
        '携程': '天台山',
        '马蜂窝': '台州天台山',
        '驴妈妈': '台州天台山',
        '飞猪': '天台山',

    },
    '根宫佛国文化旅游区': {
        '携程': '根宫佛国文化旅游区',
        '马蜂窝': '根宫佛国文化旅游区',
        '驴妈妈': '根宫佛国文化旅游区',
        '飞猪': '根宫佛国文化旅游区',

    },
    '鲁迅': {
        '携程': '鲁迅',
        '马蜂窝': '鲁迅',
        '驴妈妈': '鲁迅',
        '飞猪': '鲁迅',

    },
    '南湖': {
        '携程': '嘉兴南湖',
        '马蜂窝': '嘉兴南湖',
        '驴妈妈': '嘉兴南湖',
        '飞猪': '南湖',

    },
    '黄山': {
        '携程': '黄山',
        '马蜂窝': '黄山',
        '驴妈妈': '黄山',
        '飞猪': '黄山',

    },
    '三清山': {
        '携程': '三清山',
        '马蜂窝': '三清山',
        '驴妈妈': '三清山',
        '飞猪': '三清山',

    },
};
region_to_websites_windows = {
    '千岛湖':{

        '大众点评': '千岛湖',
        '去哪儿': '千岛湖',
        '途牛': '千岛湖',
    },
    '西湖': {

        '大众点评': '西湖',
        '去哪儿': '杭州西湖',
        '途牛': '西湖',
    },
    '西溪': {

        '大众点评': '西溪',
        '去哪儿': '西溪',
        '途牛': '西溪',
    },
    '溪口': {

        '大众点评': '溪口',
        '去哪儿': '溪口',
        '途牛': '溪口',
    },
    '乌镇': {

        '大众点评': '乌镇',
        '去哪儿': '乌镇',
        '途牛': '乌镇',
    },
    '西塘': {

        '大众点评': '西塘',
        '去哪儿': '西塘',
        '途牛': '西塘',
    },
    '横店': {

        '大众点评': '横店',
        '去哪儿': '横店',
        '途牛': '横店',
    },
    '江郎山': {

        '大众点评': '江郎山',
        '去哪儿': '江郎山',
        '途牛': '江郎山',
    },
    '雁荡山': {

        '大众点评': '雁荡山',
        '去哪儿': '雁荡山',
        '途牛': '雁荡山',
    },
    '普陀山': {

        '大众点评': '普陀山',
        '去哪儿': '普陀山',
        '途牛': '普陀山',
    },
    '南浔': {

        '大众点评': '南浔',
        '去哪儿': '南浔',
        '途牛': '南浔',
    },
    '神仙居': {

        '大众点评': '神仙居',
        '去哪儿': '神仙居',
        '途牛': '神仙居',
    },
    '天台山': {

        '大众点评': '天台山',
        '去哪儿': '台州天台山',
        '途牛': '天台山',
    },
    '根宫佛国文化旅游区': {

        '大众点评': '根宫佛国文化旅游区',
        '去哪儿': '根宫佛国文化旅游区',
        '途牛': '根宫佛国文化旅游区',
    },
    '鲁迅': {

        '大众点评': '鲁迅',
        '去哪儿': '鲁迅',
        '途牛': '鲁迅',
    },
    '南湖': {

        '大众点评': '南湖',
        '去哪儿': '嘉兴南湖',
        '途牛': '嘉兴南湖',
    },
    '黄山': {

        '大众点评': '黄山',
        '去哪儿': '黄山',
        '途牛': '黄山',
    },
    '三清山': {

        '大众点评': '三清山',
        '去哪儿': '三清山',
        '途牛': '三清山',
    },
};

























def start_spider(data_website,data_region,index):
  if (platform.system() == 'Windows'):
   os.system("python run_spider.py " + str(index) + " " + data_website + " " + data_region + " " + "景点");
  else:

   os.system("gnome-terminal -e 'bash -c \"python run_spider.py "  + str(index) +  " " + data_website
            + " " + data_region + " " + "景点" +
  "; exec bash\"'")
if(platform.system() == 'Windows'):
 website_to_search_keys = region_to_websites_windows['千岛湖'];
else:
 website_to_search_keys = region_to_websites_ubuntu['千岛湖'];
#开始结束日期
start_hour = 10;
start_minuate = 44;
index = 0;
sched = BlockingScheduler()
for key in website_to_search_keys:
    start_minuate += 5;
    if (start_minuate >= 60):
        start_minuate = 0;
        start_hour += 1;
    if (start_hour >= 24):
        start_hour = 0;
    minuate = start_minuate;
    hour = start_hour;
    print(start_minuate);
    index += 1;
    sched.add_job(start_spider, 'cron', day_of_week='0-6', hour=hour, minute=minuate, args=[key, website_to_search_keys[key], index]);
sched.start();