import os
os.system("python download_model.py AIXNS/careyou_7b_16bit_v3_2")
os.system('cd model')
os.system('ls')
os.system('cd ../')
os.system('streamlit run web_careyou.py --server.address=0.0.0.0 --server.port 7860')   