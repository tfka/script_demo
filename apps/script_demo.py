import streamlit as st
import pandas as pd
import numpy as np
import random
from PIL import Image
def app():
    st.write("# AI导演")
    st.text("剧本系统")
    #x = ["aaaa","bbbb","cccc","dddd","eeee"]
    option = st.selectbox(
        '选择一个主题',
        ('','詹姆斯在地下室中遇见了千年前穿越而来的鬼魂汤姆', '植物智慧舒缓特护安肤防敏系列，护肤品敏感肌，痘痘肌'))
    #stage =0:init stage = 1:商品show stage=2 文案show
    if option == "詹姆斯在地下室中遇见了千年前穿越而来的鬼魂汤姆":
        image = Image.open('dixiashi.png')
        title = "地下室的鬼魂"
        core = "1.詹姆斯:詹姆斯是一个退休的考古学家,他住在偏远的小镇,过着平静的生活。\n2.汤姆:汤姆是一个千年以前的鬼魂,他来到了詹姆斯的地下室。\n3.露西:露西是詹姆斯的女儿,她与汤姆成为了朋友。"
        story = "场景1.詹姆斯在地下室中发现了汤姆的日记,汤姆在日记中讲述了自己穿越千年来到现代的故事。\n场景2.汤姆在穿越过程中遇到了几个同伴,他们被困在了地下室中。\n场景3.汤姆和露西成为了朋友,露西帮助汤姆找到了回家的路。"
        details = "场景3:剧情:汤姆和露西成为了朋友,露西帮助汤姆找到了回家的路。\n地点:詹姆斯的地下室,地下室建在一个废弃工厂的废墟中,很阴暗,有大量的古董,比如花瓶、瓷器、字画等。\n对话:汤姆:\"露西,我在这儿,我是汤姆,我是一千年前的鬼魂,你不认识我了吗\"?露西:\"汤姆,你在这儿啊,你迷路了吗\"!汤姆:\"嗯,我不小心被困在了这里,你能帮帮我吗\"?"

    elif option == "植物智慧舒缓特护安肤防敏系列，护肤品敏感肌，痘痘肌":
        image = Image.open('zhiwu.jpeg')
        title = "换季敏感,怎么办?试试这款植物智慧舒缓特护安肤防敏系列!"
        core = "1.[功效]商品的核心功效是舒缓肌肤。\n2.[成分]商品含有茶树精油、芦荟、洋甘菊等成分。\n3.[适合人群]商品适合敏感肌、痘痘肌人群。"
        story = "分镜1.[商品引入]痘痘肌、敏感肌的痛点以及舒缓肌肤的重要性 \n分镜2.[商品介绍]介绍商品的功效、适合人群、成分。\n分镜3.[下单引导]介绍商品的促销活动,促进用户下单。"
        details = "1.[商品引入]:敏感肌,痘痘肌的你,是不是总是感到肌肤干燥,泛红,无光泽?那就试试这款舒缓特护安肤防敏系列吧,我敏感肌的朋友用了都说好!\n2.[商品介绍]\n\t.[适用人群] 这是一款专为敏感肌、痘痘肌设计的护肤系列,因为这款系列主打舒缓肌肤,所以适合敏感肌、有痘痘的肌肤使用。\n\t.[功效] 舒缓肌肤分为日用和夜用,日用适合白天使用,能够舒缓肌肤、抵抗紫外线,夜用适合晚上使用,可以修护肌肤、修复屏障。\n\t.[成分] 日用舒缓特护安肤乳含有茶树精油、芦荟、洋甘菊等成分,能够消炎抗菌、舒缓肌肤。夜用舒缓特润安肤霜含有积雪草、马齿苋、洋蔷薇果等成分。能够修护肌肤屏障、舒缓保湿。\n3.[下单引导]:走过路过不要错过,今天不买你睡得着吗?还不赶紧左下角小黄车加购啊,@你的闺蜜帮你付款啊。"
    if option != '':
        st.image(image)
        st.text("生成的标题是:" + title)
        st.text("核心内容是:\n" + core)
        st.text("storyline是:\n" + story)
        st.text("细节信息补充:\n" + details)

    # if "stage" not in st.session_state:
    #     # print("xxx")
    #     st.session_state.stage = 0
    # #stage = st.session_state.stage
    #
    # def id_on_click():
    #     st.session_state.stage = 1
    #
    # def gen_on_click():
    #     st.session_state.stage = 2
    # id_click = st.button("点击生成商品id",key="a", on_click=id_on_click)
    #

    #
    # # print(st.session_state)
    # if st.session_state.stage == 1:
    #     m = random.choice(x)
    #     image = Image.open('/Users/jige/heiqie/code/test.gif')
    #     st.write(str(m), "商品标题")
    #     st.image(image)
    #     st.session_state.stage = 1
    #     # stage = 1
    #     st.session_state.itemid = m
    #     st.session_state.tile = "商品标题"
    #     st.session_state.image = image
    #     if st.button("点击生成文案",key="b"):
    #         st.text("这是一个文案")
#
# print(st.session_state)
# if st.session_state.stage == 2:









# if stage == 0:
#     if st.button("点击生成商品id"):
#         m = random.choice(x)
#         image = Image.open('/Users/jige/heiqie/code/test.gif')
#         st.write(str(m), "商品标题")
#         st.image(image)
#         st.session_state.stage = 1
#         # stage = 1
#         st.session_state.itemid = m
#         st.session_state.tile = "商品标题"
#         st.session_state.image = image
#         # if st.button("点击生成文案"):
#         #     st.session_state.text = "这是一个文案"
# elif stage == 1:
#     # print("inininin")
#     if st.button("点击生成商品id"):
#         m = random.choice(x)
#         image = Image.open('/Users/jige/heiqie/code/test.gif')
#         st.write(str(m), "商品标题")
#         st.image(image)
#         st.session_state.stage = 1
#         # stage = 1
#         st.session_state.itemid = m
#         st.session_state.tile = "商品标题"
#         st.session_state.image = image
#     res = st.button("点击生成文案")
#     if res:
#         st.session_state.stage = 2
#         st.session_state.text = "这是一个文案"
#         # st.write(st.session_state.itemid, st.session_state.tile)
#         # st.image(st.session_state.image)
#         # st.text("这是一个文案")
# elif stage == 2:
#     if st.button("点击生成商品id"):
#         m = random.choice(x)
#         image = Image.open('/Users/jige/heiqie/code/test.gif')
#         st.write(str(m), "商品标题")
#         st.image(image)
#         st.session_state.stage = 1
#         # stage = 1
#         st.session_state.itemid = m
#         st.session_state.tile = "商品标题"
#         st.session_state.image = image
#     res = st.button("点击生成文案")
#     st.text("这是一个文案")
#
#     if res:
#         st.session_state.stage = 2







