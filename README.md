# quote
It is mainly used for quotations of customized products.
# 本地部署与运行
```bash
cd C:\Users\传防科电脑\Desktop\quote-main
python -m venv venv
venv\Scripts\activate
pip install streamlit
cd "C:\Users\传防科电脑\Desktop\swarm-main"
pip install .
cd "C:\Users\传防科电脑\Desktop\quote-main"
streamlit run main.py
deactivate
