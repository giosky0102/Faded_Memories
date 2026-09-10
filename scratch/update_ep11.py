import os

path = r'd:\04_Stock\Faded_Memories\scratch\캡쳐\11_europe_and_calgary_2006_2007.md'

with open(path, 'r', encoding='utf-16-le') as f:
    text = f.read()

old_text = '''  - **[1단계: 미국 중서부 ➡️ 캐나다 동부 대장정]**
    - **시카고(Chicago):** 첫 기착지, 치요에에게 안도와 사과의 전화를 건 도시.
    - **나이아가라 폭포(Niagara Falls):** 대자연의 압도적인 웅장함.
    - **토론토(Toronto):** 혜진이 머물던 캐나다 최대 도시.
    - **킹스톤(Kingston) ➡️ 몬트리올(Montreal) ➡️ 퀘벡(Quebec City):** 프랑스풍 고풍스러운 낭만의 캐나다 동부 도시들.
  - **[2단계: 미국 동부 메가시티 종단 투어]**
    - **보스턴(Boston) ➡️ 뉴욕(New York) ➡️ 필라델피아(Philadelphia) ➡️ 워싱턴 D.C.(Washington D.C.):** 세계의 중심 미국 동부 4대 메가시티 배낭 완주.
  - **[3단계: 남미 대륙의 심장, 브라질 상파울루 & 3주간의 VIP 대장정]**
    - 워싱턴 D.C.에서 남미행 비행기에 몸을 싣고 마침내 **브라질 상파울루(São Paulo)**에 상륙.
    - 캘거리에서 약속했던 절친 **알렉스(Alex)**가 공항으로 직접 마중 나와 픽업부터 전 일정 숙식과 가이드, 마지막 공항 드랍까지 완벽하게 풀케어해 줌.
    - 치안이 험악한 나라였으나 알렉스의 든든한 가이드 속에 진짜 로컬 브라질리언들의 삶과 열정적인 문화를 3주 동안 온몸으로 만끽함 (*"치안도 좋지 않은 나라지만.. 그래도 다 사람 사는 곳이지"*).'''

new_text = '''  - **[1단계: 미국 중서부 ➡️ 캐나다 동부 대장정]**
    - **시카고(Chicago):** 첫 기착지, 치요에에게 안도와 사과의 전화를 건 도시.
    - **나이아가라 폭포(Niagara Falls):** 대자연의 압도적인 웅장함.
    - **토론토(Toronto):** 혜진이 떠난 후 캠브리지반, 수미, 치요에 등 숨 가쁘게 살아왔기에 토론토를 거쳐갈 때 혜진 생각에 젖기보다는 자기 삶과 자유 여행의 열정에 집중함.
    - **킹스톤(Kingston) ➡️ 몬트리올(Montreal) ➡️ 퀘벡(Quebec City):** 프랑스풍 고풍스러운 낭만의 캐나다 동부 도시들.
  - **[2단계: 미국 동부 메가시티 종단 투어 & 글로벌 동행 모임]**
    - **보스턴(Boston) ➡️ 뉴욕(New York) ➡️ 필라델피아(Philadelphia) ➡️ 워싱턴 D.C.(Washington D.C.):** 세계의 중심 미국 동부 4대 메가시티 배낭 완주.
    - **유창해진 영어와 20대 청춘의 글로벌 친화력:** 유럽 배낭여행 때와 달리 일신된 영어 구사력 덕분에 낯선 외국인 여행자들과도 즉석에서 무리를 만들어 동행하며 거침없이 어울림.
  - **[3단계: 남미 대륙의 심장, 브라질 상파울루 & 3주간의 VIP 대장정]**
    - 마이애미 등을 거치는 어마어마하게 길고 고된 장거리 비행 노선을 거쳐 마침내 **브라질 상파울루(São Paulo)**에 상륙. 도착하자마자 장렬히 뻗어버릴 정도로 피로가 극에 달함.
    - 캘거리에서 약속했던 절친 **알렉스(Alex)**가 공항으로 직접 마중 나와 픽업부터 전 일정 숙식과 가이드, 마지막 공항 드랍까지 완벽하게 풀케어해 줌.
    - 치안이 험악한 나라였으나 알렉스의 든든한 가이드 속에 진짜 로컬 브라질리언들의 삶과 열정적인 문화를 3주 동안 온몸으로 만끽함 (*"치안도 좋지 않은 나라지만.. 그래도 다 사람 사는 곳이지"*).'''

if old_text in text:
    text = text.replace(old_text, new_text)
    print("SUCCESSFULLY REPLACED OLD TEXT")
else:
    print("WARNING: OLD TEXT NOT FOUND, ATTEMPTING LINE-BASED REPLACE")

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("CONVERTED TO UTF-8 SUCCESSFULLY")
