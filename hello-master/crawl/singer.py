from bs4 import BeautifulSoup
import re

html = '''
    <dl>
        <dt>국적</dt>
        <dd>대한민국</dd>

        <dt>활동장르</dt>
        <dd>Dance, Ballad, Drama</dd>
    
        <dt>데뷔</dt>
        <dd class="debut_song">
            <span class="ellipsis">
                2016.05.05
                <span class="bar">
                    TTT
                </span>
                <a href="#">TTTTTTTTTTTTT</a>
            </span>
        </dd>
        
        <dt>수상이력</dt>
        <dd class="awarded">
            <span class="ellipsis">
                2018 하이원 서울가요대상
                <span class="bar">|</span>본상
            </span>
        </dd>
    </dl>
'''

html2 = '''
<dl class="atist_info clfix">
    <dt>데뷔</dt>
    <dd>
        <span class="gubun">2015.05.29</span>
        <a href="javascript:;" onclick="javascript:melon.play.playSong('27120101',5712573);" title="아낀다 재생" class="btn_play_song">
            <span class="icon_play">곡재생</span>
            <span class="songname12">아낀다</span>
        </a>
    </dd>

    <dt>활동유형</dt>
    <dd>
        <span>그룹</span>
        <span>AOI</span>
    </dd>
    
    <dt>소속사</dt>
    <dd>플레디스 엔터테인먼트</dd>
    
    <dt>수상이력</dt>
    <dd class="awarded">
        <span class="ellipsis">
            2018 하이원 서울가요대상
            <span class="bar">|</span>본상
        </span>
        <a href="javascript:melon.link.goArtistDetail('861436', '2');" title="세븐틴 상세정보 더보기" class="btn_text arrow_r">
            <span class="text">더보기</span>
            <span class="icon"></span>
        </a>
    </dd>
</dl>
'''

col_names = {'국적': 'nation', '활동유형': 'act_type', '활동년대': 'act_year', '활동장르': 'act_genre', '데뷔': 'debut', '생일': 'birth', '소속사': 'company', '수상이력': 'award'}
# col_names = {'국적': 'nation', '활동유형': 'act_type', '활동년대': 'act_year', '활동장르': 'act_genre', '데뷔': 'debut', '생일': 'birth', '소속사': 'company'}

soup = BeautifulSoup(html, 'html.parser')

dl = soup.find('dl')
dts = []
dds = []
for d in dl:
    if not d.name: continue

    if d.name == 'dt':
        if not col_names.get(d.text): continue

        dts.append(col_names[d.text])
    else:
        span = d.select_one('span')
        if span != None:
            print("ssssssssssssS>>", span.text.replace('\n', ''))
            # dds.append(span.next.strip())
            
            s = span.text.replace('\n', '')
            if 'TTT' in s:
                s = s.replace('T', '')

            if '|' in s:
                s = re.sub('\s*\|', ' | ', s)
            dds.append(s.strip())
        else:
            dds.append(d.text)

vals = {}
for i in range(len(dts)):
    vals[dts[i]] =  dds[i]

print(vals)
vals = {}

for i in range(len(dts)):
    vals[dts[i]] = dds[i]

print("insert into Singer({}, {}, {}, {}) values({}, {}, {}, {});".format(
    dts[0], dts[1], dts[2], dts[3], dds[0], dds[1], dds[2], dds[3]))
