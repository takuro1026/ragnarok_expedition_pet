from ragnarok_expedition_pet import Gene, Part
from ragnarok_expedition_pet.models.polly import Polly

BASIC_POLLY = [
    Polly(num="波利1號", head="蒸蒸日上", body="精鐵原石", around="回力骨鏢"),
    Polly(num="波利2號", head="幸運葉草", body="青綠樹枝", around="冰糖葫蘆"),
    Polly(num="波利3號", head="紳士禮帽", body="閃耀冰方", around="雲霧繚繞"),
    Polly(num="波利4號", head="白雪冰晶", body="格子襯衫", around="雞毛撢子"),
    Polly(num="波利5號", head="中分棕髮", body="針織圍巾", around="法國麵包"),
    Polly(num="波利6號", head="可愛小角", body="羊毛線團", around="鋒利彎刀"),
]

GENE_LIST = [
    Gene(name="可愛小角", part=Part.HEAD, parent=["山羊犄角", "純淨獨角", "墮天之環", "櫻色貝雷", "生命冠冕"]),
    Gene(name="中分棕髮", part=Part.HEAD, parent=["山羊犄角", "雪色銀絲", "一窩雜草", "鯨泉湧動", "飄逸秀髮"]),
    Gene(name="白雪冰晶", part=Part.HEAD, parent=["純淨獨角", "雪色銀絲", "皇帝新帽", "六月飛雪", "靈光乍現"]),
    Gene(name="紳士禮帽", part=Part.HEAD, parent=["皇帝新帽", "四星大廚", "櫻色貝雷", "飄逸秀髮", "幸福小帽"]),
    Gene(name="幸運葉草", part=Part.HEAD, parent=["一窩雜草", "天使光環", "生命冠冕", "靈光乍現", "幸福小帽"]),
    Gene(name="蒸蒸日上", part=Part.HEAD, parent=["墮天之環", "鯨泉湧動", "六月飛雪", "四星大廚", "天使光環"]),
    Gene(name="羊毛線團", part=Part.BODY, parent=["白色鬍鬚", "華貴金線", "龐克潮流", "白淨襯衣", "翠綠包菜"]),
    Gene(name="針織圍巾", part=Part.BODY, parent=["白色鬍鬚", "藤條綑綁", "禦鐵王座", "雙色披風", "大汗淋漓"]),
    Gene(name="格子襯衫", part=Part.BODY, parent=["熱帶草裙", "鎖鏈鐵甲", "白淨襯衣", "雙色披風", "幻想魔方"]),
    Gene(name="閃耀冰方", part=Part.BODY, parent=["華貴金線", "青蘋果凍", "耀鏡立方", "大汗淋漓", "幻想魔方"]),
    Gene(name="青綠樹枝", part=Part.BODY, parent=["藤條綑綁", "熱帶草裙", "青蘋果凍", "苔蘚石球", "翠綠包菜"]),
    Gene(name="精鐵原石", part=Part.BODY, parent=["龐克潮流", "禦鐵王座", "鎖鏈鐵甲", "耀鏡立方", "苔蘚石球"]),
    Gene(name="鋒利彎刀", part=Part.AROUND, parent=["收割鐮刀", "雙刃精通", "拐棍糖杖", "才藝展示", "刀鋒羽翼"]),
    Gene(name="法國麵包", part=Part.AROUND, parent=["收割鐮刀", "動人音符", "流星鏈鎚", "遠行行囊", "獵人烤肉"]),
    Gene(name="雞毛撢子", part=Part.AROUND, parent=["潔白羽翼", "精靈羽翼", "刀鋒羽翼", "流星鏈鎚", "暗黑羽翼"]),
    Gene(name="雲霧繚繞", part=Part.AROUND, parent=["雙刃精通", "動人音符", "潔白羽翼", "動力滑板", "溜波波利"]),
    Gene(name="冰糖葫蘆", part=Part.AROUND, parent=["拐棍糖杖", "精靈羽翼", "環保垃圾", "遠行行囊", "溜波波利"]),
    Gene(name="回力骨鏢", part=Part.AROUND, parent=["才藝展示", "動力滑板", "環保垃圾", "獵人烤肉", "暗黑羽翼"]),
    Gene(name="山羊犄角", part=Part.HEAD, parent=["巴風特利", "詐欺波神"], children=["可愛小角", "中分棕髮"]),
    Gene(name="純淨獨角", part=Part.HEAD, parent=["七彩獨角利", "重金屬搖利"], children=["可愛小角", "白雪冰晶"]),
    Gene(name="墮天之環", part=Part.HEAD, parent=["深闇幻利", "暗黑破壞利"], children=["可愛小角", "蒸蒸日上"]),
    Gene(name="雪色銀絲", part=Part.HEAD, parent=["利尼泰美", "雙面利"], children=["中分棕髮", "白雪冰晶"]),
    Gene(name="一窩雜草", part=Part.HEAD, parent=["邋利邋遢", "原始野蠻利"], children=["中分棕髮", "幸運葉草"]),
    Gene(name="鯨泉湧動", part=Part.HEAD, parent=["桑拿波利", "利攀浪峰"], children=["中分棕髮", "蒸蒸日上"]),
    Gene(name="皇帝新帽", part=Part.HEAD, parent=["見波卸甲", "石波利"], children=["白雪冰晶", "紳士禮帽"]),
    Gene(name="六月飛雪", part=Part.HEAD, parent=["歌劇魅利", "聖誕老波"], children=["蒸蒸日上", "白雪冰晶"]),
    Gene(name="四星大廚", part=Part.HEAD, parent=["廚神波利", "關東煮仙波"], children=["紳士禮帽", "蒸蒸日上"]),
    Gene(name="天使光環", part=Part.HEAD, parent=["歐麥波利", "機利飛升"], children=["幸運葉草", "蒸蒸日上"]),
    Gene(name="白色鬍鬚", part=Part.BODY, parent=["巴風特利", "聖誕老波"], children=["羊毛線團", "針織圍巾"]),
    Gene(name="華貴金線", part=Part.BODY, parent=["潮利達人", "關東煮仙波"], children=["羊毛線團", "閃耀冰方"]),
    Gene(name="龐克潮流", part=Part.BODY, parent=["深闇幻利", "重金屬搖利"], children=["羊毛線團", "精鐵原石"]),
    Gene(name="藤條綑綁", part=Part.BODY, parent=["歐麥波利", "生命波神"], children=["針織圍巾", "青綠樹枝"]),
    Gene(name="禦鐵王座", part=Part.BODY, parent=["詐欺波神", "暗黑破壞利"], children=["針織圍巾", "精鐵原石"]),
    Gene(name="熱帶草裙", part=Part.BODY, parent=["邋利邋遢", "利攀浪峰"], children=["格子襯衫", "青綠樹枝"]),
    Gene(name="鎖鏈鐵甲", part=Part.BODY, parent=["黑酷劍利", "見波卸甲"], children=["格子襯衫", "精鐵原石"]),
    Gene(name="青蘋果凍", part=Part.BODY, parent=["玩偶小利", "利后"], children=["閃耀冰方", "青綠樹枝"]),
    Gene(name="耀鏡立方", part=Part.BODY, parent=["上流波利", "機利飛升"], children=["閃耀冰方", "精鐵原石"]),
    Gene(name="苔蘚石球", part=Part.BODY, parent=["原始野蠻利", "石波利"], children=["精鐵原石", "青綠樹枝"]),
    Gene(name="收割鐮刀", part=Part.AROUND, parent=["巴風特利", "石波利"], children=["鋒利彎刀", "法國麵包"]),
    Gene(name="雙刃精通", part=Part.AROUND, parent=["詐欺波神", "黑酷劍利"], children=["鋒利彎刀", "雲霧繚繞"]),
    Gene(name="拐棍糖杖", part=Part.AROUND, parent=["怪盜波德", "聖誕老波"], children=["鋒利彎刀", "冰糖葫蘆"]),
    Gene(name="才藝展示", part=Part.AROUND, parent=["玩偶小利", "潮利達人"], children=["鋒利彎刀", "回力骨鏢"]),
    Gene(name="動人音符", part=Part.AROUND, parent=["歌劇魅利", "重金屬搖利"], children=["法國麵包", "雲霧繚繞"]),
    Gene(name="潔白羽翼", part=Part.AROUND, parent=["歐麥波利", "七彩獨角利"], children=["雞毛撢子", "雲霧繚繞"]),
    Gene(name="精靈羽翼", part=Part.AROUND, parent=["生命波神", "利后"], children=["雞毛撢子", "冰糖葫蘆"]),
    Gene(name="動力滑板", part=Part.AROUND, parent=["潮色鹽辛利", "利攀浪峰"], children=["雲霧繚繞", "回力骨鏢"]),
    Gene(name="環保垃圾", part=Part.AROUND, parent=["天才發明利", "關東煮仙波"], children=["冰糖葫蘆", "回力骨鏢"]),
    Gene(name="櫻色貝雷", part=Part.HEAD, parent=["潮色鹽辛利", "怪盜波德"], children=["可愛小角", "紳士禮帽"]),
    Gene(name="生命冠冕", part=Part.HEAD, parent=["生命波神", "玩偶小利"], children=["可愛小角", "幸運葉草"]),
    Gene(name="飄逸秀髮", part=Part.HEAD, parent=["黑酷劍利", "利后"], children=["中分棕髮", "紳士禮帽"]),
    Gene(name="靈光乍現", part=Part.HEAD, parent=["上流波利", "天才發明利"], children=["白雪冰晶", "幸運葉草"]),
    Gene(name="幸福小帽", part=Part.HEAD, parent=["波利酋長", "潮利達人"], children=["紳士禮帽", "幸運葉草"]),
    Gene(name="白淨襯衣", part=Part.BODY, parent=["潮色鹽辛利", "利尼泰美"], children=["羊毛線團", "格子襯衫"]),
    Gene(name="翠綠包菜", part=Part.BODY, parent=["波利酋長", "廚神波利"], children=["羊毛線團", "青綠樹枝"]),
    Gene(name="雙色披風", part=Part.BODY, parent=["怪盜波德", "雙面利"], children=["針織圍巾", "格子襯衫"]),
    Gene(name="大汗淋漓", part=Part.BODY, parent=["歌劇魅利", "桑拿波利"], children=["針織圍巾", "閃耀冰方"]),
    Gene(name="幻想魔方", part=Part.BODY, parent=["七彩獨角利", "天才發明利"], children=["格子襯衫", "閃耀冰方"]),
    Gene(name="刀鋒羽翼", part=Part.AROUND, parent=["機利飛升", "暗黑破壞利"], children=["鋒利彎刀", "雞毛撢子"]),
    Gene(name="流星鏈鎚", part=Part.AROUND, parent=["波利酋長", "利尼泰美"], children=["法國麵包", "雞毛撢子"]),
    Gene(name="遠行行囊", part=Part.AROUND, parent=["邋利邋遢", "見波卸甲"], children=["法國麵包", "冰糖葫蘆"]),
    Gene(name="獵人烤肉", part=Part.AROUND, parent=["廚神波利", "原始野蠻利"], children=["法國麵包", "回力骨鏢"]),
    Gene(name="暗黑羽翼", part=Part.AROUND, parent=["深闇幻利", "雙面利"], children=["雞毛撢子", "回力骨鏢"]),
    Gene(name="溜波波利", part=Part.AROUND, parent=["上流波利", "桑拿波利"], children=["雲霧繚繞", "冰糖葫蘆"]),
    Gene(name="歐麥波利", part=Part.FINAL, children=["天使光環", "藤條綑綁", "潔白羽翼"]),
    Gene(name="上流波利", part=Part.FINAL, children=["靈光乍現", "耀鏡立方", "溜波波利"]),
    Gene(name="歌劇魅利", part=Part.FINAL, children=["六月飛雪", "大汗淋漓", "動人音符"]),
    Gene(name="波利酋長", part=Part.FINAL, children=["幸福小帽", "翠綠包菜", "流星鏈鎚"]),
    Gene(name="廚神波利", part=Part.FINAL, children=["四星大廚", "翠綠包菜", "獵人烤肉"]),
    Gene(name="機利飛升", part=Part.FINAL, children=["天使光環", "耀鏡立方", "刀鋒羽翼"]),
    Gene(name="巴風特利", part=Part.FINAL, children=["山羊犄角", "白色鬍鬚", "收割鐮刀"]),
    Gene(name="七彩獨角利", part=Part.FINAL, children=["純淨獨角", "幻想魔方", "潔白羽翼"]),
    Gene(name="潮色鹽辛利", part=Part.FINAL, children=["櫻色貝雷", "白淨襯衣", "動力滑板"]),
    Gene(name="生命波神", part=Part.FINAL, children=["生命冠冕", "藤條綑綁", "精靈羽翼"]),
    Gene(name="深闇幻利", part=Part.FINAL, children=["墮天之環", "龐克潮流", "暗黑羽翼"]),
    Gene(name="詐欺波神", part=Part.FINAL, children=["山羊犄角", "禦鐵王座", "雙刃精通"]),
    Gene(name="重金屬搖利", part=Part.FINAL, children=["純淨獨角", "龐克潮流", "動人音符"]),
    Gene(name="怪盜波德", part=Part.FINAL, children=["櫻色貝雷", "雙色披風", "拐棍糖杖"]),
    Gene(name="玩偶小利", part=Part.FINAL, children=["生命冠冕", "青蘋果凍", "才藝展示"]),
    Gene(name="暗黑破壞利", part=Part.FINAL, children=["墮天之環", "禦鐵王座", "刀鋒羽翼"]),
    Gene(name="利尼泰美", part=Part.FINAL, children=["雪色銀絲", "白淨襯衣", "流星鏈鎚"]),
    Gene(name="黑酷劍利", part=Part.FINAL, children=["飄逸秀髮", "鎖鏈鐵甲", "雙刃精通"]),
    Gene(name="邋利邋遢", part=Part.FINAL, children=["一窩雜草", "熱帶草裙", "遠行行囊"]),
    Gene(name="桑拿波利", part=Part.FINAL, children=["鯨泉湧動", "大汗淋漓", "溜波波利"]),
    Gene(name="見波卸甲", part=Part.FINAL, children=["皇帝新帽", "鎖鏈鐵甲", "遠行行囊"]),
    Gene(name="雙面利", part=Part.FINAL, children=["雪色銀絲", "雙色披風", "暗黑羽翼"]),
    Gene(name="利后", part=Part.FINAL, children=["飄逸秀髮", "青蘋果凍", "精靈羽翼"]),
    Gene(name="原始野蠻利", part=Part.FINAL, children=["一窩雜草", "苔蘚石球", "獵人烤肉"]),
    Gene(name="利攀浪峰", part=Part.FINAL, children=["鯨泉湧動", "熱帶草裙", "動力滑板"]),
    Gene(name="石波利", part=Part.FINAL, children=["皇帝新帽", "苔蘚石球", "收割鐮刀"]),
    Gene(name="天才發明利", part=Part.FINAL, children=["靈光乍現", "幻想魔方", "環保垃圾"]),
    Gene(name="聖誕老波", part=Part.FINAL, children=["六月飛雪", "白色鬍鬚", "拐棍糖杖"]),
    Gene(name="潮利達人", part=Part.FINAL, children=["幸福小帽", "華貴金線", "才藝展示"]),
    Gene(name="關東煮仙波", part=Part.FINAL, children=["四星大廚", "華貴金線", "環保垃圾"])
]


ALL_ADVANCED_GENES = filter(lambda gene: bool(gene.children), GENE_LIST)
ALL_HEAD_GENES = filter(lambda gene: gene.part == Part.HEAD, GENE_LIST)
ALL_BODY_GENES = filter(lambda gene: gene.part == Part.BODY, GENE_LIST)
ALL_AROUND_GENES = filter(lambda gene: gene.part == Part.AROUND, GENE_LIST)
