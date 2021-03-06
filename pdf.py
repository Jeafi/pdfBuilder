from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen.canvas import Canvas
import reportlab.lib.fonts
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('msyh', 'msyh.ttf'))
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table,TableStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
import time

import pdfkit

# encoding:utf-8
class LegalDocument():
    #构造函数,id,法院，当事人信息，案号，审判人员，一审法院查明
    def __init__(self):
        self.id=0
        self.fy=""
        self.dsrxx = ""
        self.dsrxxcopy = ""
        self.ah = ""
        self.ahcopy = ""
        self.spry = ""
        self.sprycopy = ""
        self.ysfycm = ""
        self.ysfycmcopy = ""
        self.ysfycmcopy2 = ""
        self.ysqqqk = ""
        self.ysqqqkcopy = ""
        self.ysqqqkcopy2 = ""
        self.byrw = ""
        self.byrwcopy = ""
        self.byrwcopy2 = ""
        self.spjg = ""
        self.spjgcopy = ""
        self.spjgcopy2=""
        self.ysdbqk = ""
        self.ysdbqkcopy = ""
        self.ysdbqkcopy2 = ""
        self.esqqqk = ""
        self.esqqqkcopy = ""
        self.esqqqkcopy2 = ""
        self.ysfyrw = ""
        self.ysfyrwcopy = ""
        self.ysfyrwcopy2 = ""
        self.wslx = ""
        self.ajms = ""
        self.ajmscopy = ""
        self.ajmscopy2 = ""
        self.xgft = ""
        self.xgftcopy = ""
        self.sprq = ""
        self.sprqcopy = ""
        self.sljg = ""
        self.sljgcopy = ""
        self.sljgcopy2 = ""
        self.bycm = ""
        self.bycmcopy = ""
        self.bycmcopy2 = ""
        self.sjy = ""
        self.sjycopy2 = ""
        self.bt = ""
        self.btcopy = ""
        self.fycj = ""
        self.dy = ""
        self.nf = ""
        self.slcx = ""
        self.ay = ""
        self.ft = ""
        self.tz = ""
        allSearchFieldList = {"当事人信息": "dsrxx", "案号": "ah", "审判日期": "spry", "一审法院查明": "ysfycm", "一审请求情况": "ysqqqk",
                              "本院认为": "byrw", "审理经过": "spjg", "一审答辩情况": "ysdbqk", "二审请求情况": "esqqqk",
                              "一审法院认为": "ysfyrw", "案件描述": "ajms", "相关法条": "xgft", "审判日期": "sprq", "审理经过": "sljg",
                              "本院查明": "bycm", "书记员": "sjy", "标题": "bt"}

legalDocument = LegalDocument()
legalDocument.id=0
legalDocument.fy = "法院"
legalDocument.dsrxx = "公诉机关山东省莱芜市人民丘市人，捕前租住河北省廊坊市。2012年12月23日被山东省章丘检察院批准，于次日被莱芜市公安局莱城分局依法执行逮捕。辩护人田英莲，山东众诚仁和（莱芜）律师事务所律师。"
legalDocument.ah = "（2013）莱中刑一初字第5号"
legalDocument.spry = "黎柏林"
legalDocument.ysfycm = "一审法院查明"
legalDocument.ysqqqk = "辩护人的辩护意见是：1、被告人无杀害被害人王某甲的故意，不构成故意杀人罪；2、被害人有重大过错；3、被告人系初犯、偶犯，案发后认罪悔罪、积极赔偿被害人经济损失，并取得被害人方谅解，应从轻、减轻处罚。"
legalDocument.byrw = "本院认为，被告人马振家因债务纠纷故意杀害他人，致一人死" \
                     "亡，其行为已构成故意杀人罪。公诉机关指控的事实和罪名成立，本院予以确认。鉴于被告人马振家到案后能够如实供述自己的主要犯罪事实，属坦白；案" \
                     "发后，被告人亲属积极赔偿被害方经济损失21万元，取得被害人亲属的谅解，综合全案的具体情节和被告人马振家的认罪悔罪态度，可酌情对其从轻处罚。依照1979年《中华人民共和国刑法》第一百三" \
                     "十二条、《中华人民共和国刑法》第十二条、第六十七条第三款、第五十七条第一款的规定，判决如下："
legalDocument.spjg = "被告人马振家犯故意杀人罪，判处无期徒刑，剥夺政治权利终身。如不服本判决，可在接到判决书的第二日起十日内，通过本院或者直接向山东省高级人民法院提出上诉。书面上诉的，应提交上诉状正本一份，副本三份。"
legalDocument.ysdbqk = "被告人马振家对公诉机关指控的故意杀人罪的罪名和事实均提出异议，称没有杀害被害人的故意，事情起因系被害人首先对其殴打所致。"
legalDocument.esqqqk = "辩护人的辩护意见是：1、被告人无杀害被害人王某甲的故意，不构成故意杀人罪；2、被害人有重大过错；3、被告人系初犯、偶犯，案发后认罪悔罪、积极赔偿被害人经济损失，并取得被害人方谅解，应从轻、减轻处罚。"
legalDocument.ysfyrw = "一审法院认为"
legalDocument.wslx = "wslxwslx"
legalDocument.ajms = "案件描述案件描述案件描述"
legalDocument.xgft = "相关法条相关法条相关法条"
legalDocument.sprq = "二〇一三年六月二十七日"
legalDocument.sljg = "山东省莱芜市人民检察院以莱检公刑诉（2013）5号起诉书指控被告人马振家犯故意杀人罪，于2013年4月22日向本院提起公诉。本院依法组成合议庭，于2013年5月28日公开开庭进行了审理。莱芜市人民检察院指派代理检察员柳冬梅、吕晓出庭支持公诉。被告人马振家及其辩护人田英莲到庭参加诉讼。现已审理终结。"
legalDocument.bycm = "经审理查明：被告人马振家1996年曾受王某甲（男，山东省章丘人，殁年41岁）雇佣为其开货车跑运输。1997年7月18日凌晨2时许，被告人马振家驾驶车牌号为鲁A60&times;&times;&times;的解放141货车与王某" \
                     "甲一起到莱芜市莱城区A镇拉沙，行至A镇B村路段时，两人因欠款纠纷等问题发生争吵，继而在驾驶室内厮打。期间，被告人马振家持车摇把多次砸击王某甲头、面部，后趁王某甲下车之机，开车将其撞倒在路边玉米地" \
                     "里并碾压其右胸部，致被害人王某甲创伤性休克死亡。被告人马振家于当日凌晨五时许将车开回王某甲家院内，后驾驶王某甲的摩托车潜逃。2012年12月22日被告人马振家在河北省廊坊市其租房处被山东省章丘市公安局民警" \
                     "抓获。上述事实，有下列证据予以证实：（一）证人证言1、朱某某证实，1997年7月18日早晨6点10分左右，在王某甲汽修部门前，听本村李某甲说前面压死了一个人。出事地点在莱明路B村村委办公室南300米左右公路东边的玉" \
                     "米地里，离公路约有5米左右，地里趴着一名男子，头西脚东，脖子上有血，上穿白背心，下穿蓝裤子，公路上有一双红色皮凉鞋，现场有许多车印，玉米地里也有，于是就报案了。2、李某乙证实，其在A镇某修理厂工作，1997年7月" \
                     "18日早上4点左右，一个新泰的司机叫其去修车，当行至丁字路口时那个新泰人说：&ldquo;你看这地方这个车（指路边车印）在这弄的&rdquo;，其顺他说的方向发现一个人头西脚东在地上趴着，看样子死了，路边有两只棕红" \
                     "色的皮凉鞋，公路上的车印、泥还挺新鲜，车印多而杂，其吓得赶紧走了。当时在场的就其和新泰那个人，后来朱某甲也过来看了。3、穆某某证实，其系王某甲妻子，1996年其家雇的马振家开车，开了大半年，处的关系也" \
                     "挺好，今年马振家自己买了汽车搞运输，可能没赚到钱，报停了。今年7月5号他又来其家开车。1997年7月17日晚上，马振家在其家里吃的饭，18日早晨两点钟其对象到学校叫上马振家，他们两个人开车走的。早晨5点钟左" \
                     "右马振家来叫门，说&ldquo;俺哥去找人，得修车，车漏油挺厉害，我再去要帐&rdquo;，他就到学校骑着其家里的红色K90摩托车走了，5点30分左右其到车前，看到车门子上有血，拉开车门子见里面乱七八糟的，有好多血" \
                     "迹，其赶紧叫的邻居，又去学校叫起王某乙，然后打110报案。同时证实，马振家自己搞运输没赚着钱，欠人家的钱人家跟他要，人家欠他的钱他要不上来。十几天前其对象借给他二千块钱，他说是还帐，因为7月20日其家里" \
                     "也要还帐用钱，从7月15日开始其跟他要了几次钱，他答应还，这几天他也没借着钱。1997年4月，其对象被朋友骗到深圳去搞传销，5、6月份回来的，7月17日下午，其对象说&ldquo;你看看他（马振家）就跟死了爹似的，" \
                     "就好像我欠他钱似的&rdquo;，其猜可能是其对象跟马振家要帐了。4、王某乙证实，其系王某甲儿子，1997年7月17日下午说好第二天早上其跟马振家一起去莱芜拉沙，不知道为什么没叫他，18日早上其母亲穆某某把其叫" \
                     "起来的，说&ldquo;你快起来，咱的车里有血，你爸也没回来，可能出事了。&rdquo;其一听就赶紧起来，发现腰带没了，当时车在院子里停着，挡风玻璃和地板上有大量血迹。后来记不清是谁开着车带其去了莱芜医院辨认" \
                     "尸体，其认出是父亲。17日晚上马振家拖着凉席在外面睡的觉，其父亲可能在外面说过马振家欠钱没还的事，可能马振家听见了，所以对其父亲有意见，才想害其父亲。5、高某某证实，其系马振家妻子，马振家1996年给王某甲" \
                     "开了一年车，春节后不给他干了，最近才去了一个多月时间。去年冬季，其对象借了王某甲5000元钱，自己买了一辆东风汽车单干，但最近一个时期找不到活，加上王某甲多次来要帐，因没钱还，最后马振家又回去给他开车，" \
                     "。马振家从昨天（1997年7月17日）早晨走后就没再回来。（二）现场勘查记录证实现场位于章莱路A镇B村西南，尸体至路沿8.4米，轮胎印西侧4米、东侧5米，尸体距沟西沿4.9米，沟上宽2米，深0.6米，底宽1.2米，南轮进地1." \
                     "4米，北轮进地柴垛至尸体头部6.4米，至轮印3.4米。另有现场方位图、现场照片24张在案佐证。（三）鉴定结论1、莱芜市公安局莱城分局莱城公技（法）字（97）第62号法医学鉴定书证实：①死者面部广泛挫伤并有多处裂创，上" \
                     "下颌骨骨折，右胸壁塌陷，多肋骨骨折，右肺挫裂伤。全身皮肤粘膜苍白，尸斑不明显，脾皱缩苍白。分析系创伤性休克死亡。②据尸检，死者头面部多处裂创均创缘不齐，创腔内有组织间桥，符合钝器打所致。前颈胸部皮下出血" \
                     "，右胸壁塌陷，多肋骨骨折，符合巨大外力挤压所致。结论：王某甲系创伤性休克死亡。2、莱芜市公安局莱城分局检验报告证实，伤者（马振家）神志清，查体合作，左颅顶部见1.8cm的陈旧性不规则疤痕。右眉上方见2.6cm的陈旧" \
                     "性不规则疤痕。颏部见1.2cm的陈旧性不规则疤痕。牙齿1┿12装有义齿。左手大鱼际处见2cm的陈旧性疤痕。右拇指背侧见1cm的陈旧性疤痕。马振家自述，上述疤痕均为1997年7月18日其受伤后所留，于2013年2月28日，在莱芜市看" \
                     "守所对其上述疤痕拍照固定。（四）综合证据1、刑事案件立案报告表、受理刑事案件登记表各1份，证实公安机关接处警情况。2、章丘市公安局抓获笔录、移交说明各1份，证实公安机关抓获马振家的情况。3、莱芜市公安局莱城分" \
                     "局发破案经过、刑警大队侦查工作情况说明各1份，证实案件侦破情况。4、章丘市公安局刑警大队情况说明1份，证实抓获马振家的过程。2012年12月22日，马振家在河北省廊坊市落网，12月23日羁押于章丘市看守所。莱芜市公安局" \
                     "莱城分局民警于12月26日将马振家押回。5、户籍证明、死亡证明各1份，证明被告人马振家、被害人王某甲的基本情况。6、提取物品笔录证实，1997年7月18日11时30分，在章丘市公安局某派出所院内停放的蓝色解放牌141型（鲁A" \
                     "-60&times;&times;&times;）货车驾驶室内提取以下物品：10号扳手1个，梅花螺丝刀1个，车摇把1个，千斤顶1个，行车水壶1个，三节手电筒1个，带血迹的白底兰花短袖T恤1件，玻璃水杯1个，小黑手提包1个，牙齿两颗。" \
                     "。另有拘留证、拘留通知书、延长拘留期限通知书、批准逮捕决定书、逮捕证等书证，在案佐证。（五）被告人马振家供述与辩解我从1994年开始给王某甲开车开了两年半，1996年冬天我自己买了一辆车，偶尔也帮王某甲出车。19" \
                     "97年7月18日凌晨，当时我在章丘市给王某甲开车，王某甲到我和他儿子睡觉的屋里叫我出车，他让我跟他一起去莱芜拉沙，我们开着解放牌货车，王某甲坐在副驾驶上，走到莱芜雪野湖附近时，因原来我借过王某甲3000元钱，王某" \
                     "甲突然要我还钱，我说还了，他还说了一些其他难听的话，我们就吵了起来，王某甲脾气很暴并先动手打我，先用拳头打我的头，又把我的头往方向盘上撞，后来又用车上的摇把子抽我的后背，把我打急了，我就夺过摇把子往他头上" \
                     "砸，也记不清砸了几下，也没看清打的什么样，光看见脸上有血，王某甲把我从车上踢了下来，我下车后，王某甲又开车撞我，把我撞倒在了路边的玉米地里，王某甲可能是想下车看看我怎么样了，我趁机上了车，王某甲也没拦我，" \
                     "，但是倒不动，为了能跑，虽然看见王某甲站在车前面我还是往前开撞了他，后来好像又压到他了，当时光想跑了，我也没管他，然后就开车跑回章丘，把车放到王某甲家才跑的。上述证据，均经法庭举证、质证，本院予以确认。针" \
                     "对控辩双方的争议焦点，分别评判如下：关于被告人及其辩护人提出的&ldquo;被告人的行为不构成故意杀人罪&rdquo;的辩解、辩护意见，经查，被告人马振家与被害人王某甲因欠款纠纷等问题在车内发生争吵，继而在驾驶室内发" \
                     "生厮打。期间，被告人马振家持车摇把多次砸击被害人头、面部，致被害人面部广泛挫伤并有多处裂伤，上下颌骨骨折。上述事实有被告人供述、被告人与被害人身体上的伤情、勘查发现驾驶室内血迹、" \
                     "。尸体检验报告证实王某甲身体右胸壁塌陷、肋骨骨折，符合巨大外力挤压所致，与被告人供述用车撞倒王某甲后碾压被害人的事实、及车辆勘查在右前盖和右前轮、右后轮的血迹等相吻合。以上证据相互印证，证实被告人趁被害人" \
                     "王某甲下车之机，开车将王某甲撞倒在路边玉米地里并碾压其右胸部，致被害人王某甲创伤性休克死亡。被告人明知驾驶车辆碾压他人的后果而实施这一行为，其行为构成故意杀人罪。被告人及其辩护人的相关辩解、辩护意见不能成" \
                     "立，不予采纳。关于被告人及其辩护人提出的&ldquo;被害人具有重大过错&rdquo;的辩解、辩护意见，经查，现有证据只能证明被告人与被害人因欠款纠纷等问题在车内发生争吵并厮打，没有证据证明被害人有重大过错。被告人及" \
                     "其辩护人的辩解、辩护意见不能成立，不予采纳。"
legalDocument.sjy = "书记员范振英"
legalDocument.bt = "马振家故意杀人一审刑事判决书"
legalDocument.fycj = "法院层级"
legalDocument.dy = "dydydyd"
legalDocument.nf = "nfnfnfnf"
legalDocument.slcx = "slcx"
legalDocument.ay = "ayay"
#临时文件名
curr_date = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
css=r'D:\pdfBuilder\showDetail.css'
options={
    'page-size':'Letter',
    'margin-top':'0.75in',
    'margin-right':'0.75in',
    'margin-bottom':'0.75in',
    'margin-left':'0.75in',
    'encoding':"UTF-8",
    'no-outline':None
}
path_wk = r'C:\Users\jeafi\Desktop\wkhtmltopdf\bin\wkhtmltopdf.exe' #安装位置
config = pdfkit.configuration(wkhtmltopdf = path_wk)
#读文件并且替换动态内容
fp = open("pdf.html",'w',encoding = 'utf-8')  #打开你要写得文件test2.txt
lines = open('demo.html','r',encoding = 'utf-8').readlines()  #打开文件，读入每一行
for s in lines:
    fp.write( s.replace("标题",legalDocument.bt)
              .replace('diyu',legalDocument.dy)
              .replace('dangshirenxingxi',legalDocument.dsrxx)
              .replace('anjianmiaoshu',legalDocument.ajms)
              .replace('shenlijingguo',legalDocument.sljg)
              .replace('yishenqingqiuqingkuang',legalDocument.ysqqqk)
              .replace('yishendabianqingkuang',legalDocument.ysdbqk)
              .replace('yishenfayuanchaming',legalDocument.ysfycm)
              .replace('yishenfayuanrenwei',legalDocument.ysfyrw)
              .replace('ershenqingqiuqingkuang',legalDocument.esqqqk)
              .replace('benyuanchaming',legalDocument.bycm)
              .replace('benyuanrenwei',legalDocument.byrw)
              .replace('shenpanjieguo',legalDocument.spjg)
              .replace('shenpanrenyuan',legalDocument.spry)
              .replace('shenpanriqi',legalDocument.sprq)
              .replace('shujiyuan',legalDocument.sjy)
              .replace('xiangguanfatiao',legalDocument.xgft))    # replace是替换，write是写入
fp.close()  # 关闭文件

pdfkit.from_file('pdf.html', options=options, css=css,output_path = 'out%s.pdf'%(curr_date), configuration=config)
# can = SimpleDocTemplate("out%s.pdf"%(curr_date))
# content = []
# stylesheet=getSampleStyleSheet()
# normalStyle = stylesheet['Normal']
# #写内容
# rpt_title = '<para autoLeading="off" fontSize=15 align=center><b><font face="msyh">%s</font></b><br/><br/><br/></para>' % (legalDocument.bt)
# content.append(Paragraph(rpt_title, normalStyle))
# content.append(Paragraph('<para autoLeading="off" fontSize=8><font face="msyh" >基本信息：</font><br/>',normalStyle))
#
# # data = [["案号",legalDocument.ah,"文书类型",legalDocument.wslx],
# #         ["年份",legalDocument.nf,"审理程序",legalDocument.slcx],
# #         ["地域",legalDocument.dy,"法院层级",legalDocument.fycj]]
# # # #创建表格对象，并设定各列宽度
# # # component_table = Table(data, colWidths=[50,170,50, 170])
# # # #添加表格样式
# # # component_table.setStyle(TableStyle([
# # # ('FONTNAME',(0,0),(-1,-1),'msyh'),#字体
# # # ('FONTSIZE',(0,0),(-1,-1),6),#字体大小
# # # ('SPAN',(0,0),(3,0)),#合并第一行前三列
# # ('BACKGROUND',(0,0),(0,0), colors.lightskyblue),#设置背景颜色
# # ('BACKGROUND',(0,1),(0,1), colors.lightskyblue),#设置背景颜色
# # ('BACKGROUND',(0,2),(0,2), colors.lightskyblue),#设置背景颜色
# # ('BACKGROUND',(2,0),(2,0), colors.lightskyblue),#设置背景颜色
# # ('BACKGROUND',(2,1),(2,1), colors.lightskyblue),#设置背景颜色
# # ('BACKGROUND',(2,2),(2,3), colors.lightskyblue),#设置背景颜色
# # # ('SPAN',(-1,0),(-2,0)), #合并第一行后两列
# # ('ALIGN',(-1,0),(-2,0),'RIGHT'),#对齐
# # ('VALIGN',(-1,0),(-2,0),'MIDDLE'),  #对齐
# # ('LINEBEFORE',(0,0),(0,-1),0.1,colors.grey),#设置表格左边线颜色为灰色，线宽为0.1
# # ('TEXTCOLOR',(0,1),(-2,-1),colors.royalblue),#设置表格内文字颜色
# # ('GRID',(0,0),(-1,-1),0.5,colors.black),#设置表格框线为红色，线宽为0.5
# # ]))
# #
# #
#
#
#
# content.append(component_table)
# can.build(content)
