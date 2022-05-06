from turtle import down
import urllib.request
import threading
import time
# https://1movieshd.com/watch-tv/free-the-troop-hd-35496.5204686
Download_Links = {
                  'S01E01':'https://www-u8s35747.ssl0d.com/ooOOKf4Prxr7Zib5mYeOMg/1651813448/I5EXWkZmjUyMzZG-tzFHnppt_6PXGnyOAVi3tdctaR1BH7IW8opAGFVrG1iI4edYJiZeB8gRAfYTbpiiinI5Brcz5IUwJpDBj7UTtzy6j_8D0Q6GIlpDjlY3g4t5nX35M3YSmaB2Yr1RzCwRRyuUHuD-8adeCTs0lvtkumLSHgv7Uc4l2Umf1xJ0OsoduOos9UGMMA1dEm1LTLhK-InxhZJo0MxNxvAI0fmX4l0yXn1fy9pfxz6Vw3YZEpSUo8TWB917aJWlgNAhwR3f7oZhAg/7066762.mp4?dl=1',
                #   'S01E02':'',
                  'S01E03':'https://www-26i32386.ssl0d.com/4fvCIoU0bARBvKDLmUSDiw/1651813787/I5EXWkZmjUyMzZG-tzFHnppt_6PXGnyOAVi3tdctaR1-RdqYjhSgevPEjY8P90XWCTdJwWLi_igIpYVSliQ3mPbSQu6hOsCz5tFmEebuKeLG-kRIPNr2N0MOvTJwziWFSd_6eWYWIVPrZGD4u9dEDIj-T32I7UWPl4m5bGx0aF3OmBO8HUezToMKgmMyjh8UNul7wc-lwEQ97pMoss08bVtFiR0hr9uCmktVzNWDVpB1bSrrSIlBuhiEGZviZUXJH73eXKwAzqx4ogo_Q9hwmw/7066771.mp4?dl=1',
                  'S01E04':'https://www-vfj4191.ssl0d.com/0iXSPb0Wi6FTefjVpaCxiQ/1651813857/I5EXWkZmjUyMzZG-tzFHnppt_6PXGnyOAVi3tdctaR0n0qvRpGtgRRS7z-a9ItxsQh_izXPa0vlRTxVDXMkTEYlhDKTSM0j4i8RtjlXw1bOauMl3H8wXApk9oOZI_vH2z9_rnEJMNaJGN1bZxNJeQxenzkUC0N3YTQfMo-dVcsIYim4-daDgHeOv1Y3fypIvQtFSIvtMYBwdr34-2VQxfEZk9t5Xr7QKF-VkjLnkB1hg66nTNTE2l1EQjrk0y2SfbjSLWnxzb_u3FcNvmAElmA/7066774.mp4?dl=1',
                  'S01E05':'https://www-26i32386.ssl0d.com/nlbnphl4EyCfpo_Y4pbVuw/1651813913/I5EXWkZmjUyMzZG-tzFHnppt_6PXGnyOAVi3tdctaR1wosKUUs2kiHJPad7_i5wGUcB6ORQSmGhc0RVzyWBzQlo2a7v2UWbjSr-TiAgLTitCmXRSEv7oAiArBhSaGFXpZej2f2_LdVn3Yzk_Fqskt1_VqzO7Jwq7O7HbG-2Nfch7qLMdiPLkChqNTPXAfFiH_2TYWRP7NLYlk-RREokkubAxeM-DEoVgZj3fofFgJqQ_dtlCXkUS3r0eaO-ORFAd6ZFgZ1cLkKT76a0k5xH40A/7066777.mp4?dl=1',
                  'S01E06':'https://www-dvc10735.ssl0d.com/u0UJRKhz5F1krMalbx1toA/1651814004/I5EXWkZmjUyMzZG-tzFHnppt_6PXGnyOAVi3tdctaR38MFS3RPkDXsMX1-e9a6XNZOP0Jg9--EiAVGMRASAEdH9rWtQCqnaSRw79zfs-hNIIA7AXKP90jQOf_i9vnjOujtFIt8hHVvL2yRHb8yAzHpDgdgXP7EX4QznpwaAawYOGu3a_wfqR6wb3fIk6V2sBzX1jQOMERJ_8UMbu974jEwR-PLvhK9X3NHmjGgc45jEzPliGGHCRqaTZ-DO75AsliB2lovtxWkAXARZwKcO9ew/7066783.mp4?dl=1',
                  'S01E07':'https://www-m01706.ssl0d.com/13zl0P0WfsnrC5Yo2pE9Jg/1651814116/I5EXWkZmjUyMzZG-tzFHnppt_6PXGnyOAVi3tdctaR0yrtZrMuqC-DRaqoILEd45g6mWXnIL3tCogw-pz_bgQ-cYmjK5tp6gkNo78KSM2FjSDBFExYYMCkKq3puyq473dVoBo-w2FoSMsT57rzf7DWb7f2o1yCXKVu-fQw8TNPFq2wrncqcCRXNAPiErKQxnP20RNjCVKQVoGjWC8vZgPfA-0QacGFODknwu4-o2w1OA9hFBYSV-ABvlIfREc88JEjR2SlZvdb7ORHPftzhblg/7066780.mp4?dl=1',
                  'S01E08':'https://www-u8s35747.ssl0d.com/mSZ1YsisC6g4W0jLevjtOw/1651814294/I5EXWkZmjUyMzZG-tzFHnppt_6PXGnyOAVi3tdctaR1L2P4cAymmj7SBW5AVQup2aVDTvtIIu7qRwWu_vNlnjVgTzVQ6mv62G92TO7FWTQNw7E2boAKGxZmDouoAHz_9G4T0sukGbKyUn2g4U8j7I3t-vTjE5JjZZimwPUkGOImkk_Q1U2l3QcDqjJB1jrUdbpm25986adct0tGo0H_kZgvRY-TgnWv01lNB_22QDdxbcJjkjQi7hJ7slvwhHK1iLkMXeNScoAUU9OtpkIffnQ/7066786.mp4?dl=1',
                  'S01E09':'https://www-hjt8627.ssl0d.com/KhzxhXurXo2jAc7rcHOdBg/1651814324/I5EXWkZmjUyMzZG-tzFHnppt_6PXGnyOAVi3tdctaR1i9Q9MOoAOLd1ZGA1szU7-wKwR4Br95No4dE_MuGxIML5pysDTrG2it_k91G8NdHIu9eg50wcpGY-FVcMlfaXUp-9wgyxP8Rfos1fUXkJomuXEoyOL9gcddO2899cLi3sne_QJYHMJNbZZF2M6ID7xEXaBb4Uf2LZ-k5llIwkSdWodGfi_tlIJG1WQZfr2lLBRJVk-VAyPDyyrswMITNbtRVgZZ1_OzFHCWE019lDvpw/7066789.mp4?dl=1',
                #   'S01E10':'',
}
threadList =[]

def download_video(Episode_number,dwn_link):
    file_name =f'Firends With Better Lives Episode {Episode_number}.mp4'
    urllib.request.urlretrieve(dwn_link, file_name)
    print(f'{file_name} : Downloaded Complete')

for number,link in Download_Links.items():
    thread= threading.Thread(target=download_video,args=(number,link,))   
    print(f'Episode : {number} Added')
    threadList.append(thread)
for thread in threadList:
    thread.start()
    print('downloading started')
for thread in threadList:
    thread.join()    
print("done")