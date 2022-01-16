import pandas as pd

#pip install openpyxl

data = [
          ["Ahmet Yılmaz","İnsan Kaynakları",30,"Kadıköy",5000],
          ["Can Ertürk","Bilgi İşlem",25,"Tuzla",3000],
          ["Hasan Korkmaz","Muhasebe",45,"Maltepe",4000],
          ["Cenk Saymaz","Bilgi İşlem",50,"Tuzla",3500],
          ["Ali Turan","İnsan Kaynakları",23,"Kadıköy",2750],
          ["Rıza Ertürk","Muhasebe",34,"Tuzla",6500],
          ["Mustafa Can","Bilgi İşlem",42,"Maltepe",4500]
       ]

df = pd.DataFrame(data,columns=["Çalışan","Departman","Kişi_Yaşı","Bölge_Semt","Aylık_Maaş"])

df.to_excel("C:\\Users\\Mehmet KAHRAMAN\\Desktop\\export.xlsx", sheet_name="Sayfa1", index=False, header=True)