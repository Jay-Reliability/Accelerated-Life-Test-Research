import os
import streamlit as st
import streamlit.components.v1 as components

# 1. Streamlit 페이지 기본 환경 설정 (와이드 모드 및 탭 타이틀/파비콘 설정)
st.set_page_config(
    page_title="전자제품 핵심부품 신뢰성 가속수명시험 연구동향",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Streamlit 상단 여백 및 기본 패딩 최소화 (전체 화면 최적화)
st.markdown("""
    <style>
        /* 불필요한 기본 여백 제거 및 배경색 통일 */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        header[data-testid="stHeader"] {
            display: none !important;
        }
        footer {
            visibility: hidden !important;
        }
    </style>
""", unsafe_allow_html=True)

# 3. HTML 파일 로드 함수 (캐싱 적용으로 속도 최적화)
@st.cache_data
def load_html_content(file_path: str) -> str:
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        return f"""
        <div style="color: #f87171; background: #1e293b; padding: 24px; border-radius: 8px; font-family: sans-serif;">
            <h3>⚠️ HTML 파일을 찾을 수 없습니다.</h3>
            <p>저장소 루트 폴더에 <code>21_ALT_Google_Web_Hosting_2_final.html</code> 파일이 존재하는지 확인해 주세요.</p>
        </div>
        """

# 4. 파일 읽기 및 렌더링
html_file_name = "21_ALT_Google_Web_Hosting_2_final.html"
html_content = load_html_content(html_file_name)

# Streamlit Components를 통해 iframe 격리 환경에서 자바스크립트 및 인터랙티브 UI 실행
components.html(html_content, height=1400, scrolling=True)