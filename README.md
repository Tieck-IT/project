<proeject list>

# 분류 모델 평가 지표  
  
  - 정확도 : 옳게 예측한 비율
  
  ![image](https://user-images.githubusercontent.com/90205987/147515859-d907a5b9-3895-481c-aebd-1974b02204e5.png)

  
  
  - 정밀도 : 실제 중 [(예측 : 양성) -> (실제 : 양성) ] 예측 비율
  
  ![image](https://user-images.githubusercontent.com/90205987/147515826-a0cef040-97c9-4fd0-be46-3df552f077a2.png)

  
  - 재현율 : 실제 양성(Positive) 중  [(예측 : 양성) -> (실제 : 양성) ] 예측 비율
  
  ![image](https://user-images.githubusercontent.com/90205987/147515828-e5b5216c-79de-4830-b2fe-a6aeb9358721.png)
 
  - F1 score : 정밀도와 재현율의 조화평균 (불균형 라벨의 평가 보완)
  ![image](https://user-images.githubusercontent.com/90205987/147515835-439fc4a7-075d-44f8-8477-ce124718e9d5.png)

    
  - 손실  그래프
  - 정확도 그래프
  - aucroc

# [당뇨병 위험 예측 모델](https://github.com/Tieck-IT/proeject/tree/master/PredictDiabetes)
  - 임상검사와 방문없이, 설문조사 데이터를 이용해 예측 모델 훈련
  - 사용 데이터 : 교육용 데이터 from [질병관리청 국립보건연구원](https://www.kdca.go.kr/contents.es?mid=a40504070100)
    - Accuracy : 0.9295
    - AUCROC : 0.7831
    - F1 score : 0.8875
    - Recall : 0.2340
    - Precision : 0.22
  
      ![image](https://user-images.githubusercontent.com/90205987/147515793-c54ecf7d-d6cb-4aaa-a669-0d03f9b62411.png)

  
