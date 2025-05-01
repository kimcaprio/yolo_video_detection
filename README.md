# YOLO 기반 보호장구 감지 시스템

이 프로젝트는 YOLO 객체 감지 모델을 사용하여 특정 공간에서 사람의 보호장구(헬멧) 착용 여부를 실시간으로 감지하고 알람을 제공하는 시스템입니다.

## 기능

- 실시간 비디오 스트림에서 사람과 보호장구 감지
- 보호장구 미착용 시 시각적 알람 제공
- FPS 모니터링
- 실시간 결과 시각화

## 설치 방법

1. 저장소 클론:
```bash
git clone [repository-url]
cd yolo_video_detection
```

2. 필요한 패키지 설치:
```bash
pip install -r requirements.txt
```

3. YOLO 모델 가중치 다운로드:
- `data/weights` 디렉토리에 YOLO 모델 가중치 파일을 배치
- 기본적으로 `yolov8n.pt` 모델을 사용하도록 설정되어 있음

## 사용 방법

1. 웹캠을 사용하는 경우:
```bash
python src/main.py
```

2. 비디오 파일을 사용하는 경우:
- `main.py` 파일에서 `VideoCapture(0)`을 `VideoCapture('video_path')`로 수정

## 주의사항

- 모델의 클래스 ID는 데이터셋에 따라 다를 수 있으므로 `detector.py`에서 적절히 수정 필요
- 실시간 성능을 위해 적절한 하드웨어 권장
- 알람 시스템은 현재 시각적 알람만 구현되어 있음

## 라이선스

MIT License 