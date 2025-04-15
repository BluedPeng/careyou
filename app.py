import os
os.system("python download_model.py AIXNS/careyou_7b_16bit_v3_2")
os.system('cd model & ls')
os.system('pwd')
os.system('streamlit run web_careyou.py --server.port 8053')   