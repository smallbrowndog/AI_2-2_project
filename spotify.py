import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


client_credentials_manager = SpotifyClientCredentials(client_id='648bd29bb43f4c019720b5dc343e8f00', client_secret='26a67f2bae554ee4a8be8f11a22903cc')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

rec = sp.recommendations(seed_genres=["k-pop"],seed_tracks=["5sdQOyqq2IDhvmx2lHOpwd"], market=["KR"], limit=50, min_tempo=[50], max_tempo=[200], max_popularity=[100])

# 빈 리스트를 생성하여 트랙 정보를 저장할 변수 생성
track_info_list = []

# 트랙 정보를 리스트에 저장
for track in rec['tracks']:
    track_info = f"{track['artists'][0]['name']} / {track['name']}"
    track_info_list.append(track_info)

# 결과 확인
for track_info in track_info_list:
    print(track_info)