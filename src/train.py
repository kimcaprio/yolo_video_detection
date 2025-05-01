from ultralytics import YOLO
import os

def main():
    # YOLO 모델 초기화 (YOLOv8 사용)
    model = YOLO('yolov8n.pt')  # 작은 모델로 시작
    
    # 학습 설정
    results = model.train(
        data='/Users/clouderakr/Downloads/yolo_video_detection/data/helmet_dataset/data.yaml',  # 절대 경로로 수정
        epochs=5,  # 학습 에포크 수
        imgsz=640,  # 이미지 크기
        batch=16,  # 배치 크기
        device='0' if os.environ.get('CUDA_VISIBLE_DEVICES') else 'cpu',  # GPU 사용 가능시 GPU 사용
        project='runs/train',  # 결과 저장 디렉토리
        name='helmet_detection',  # 실험 이름
        exist_ok=True,  # 이미 존재하는 디렉토리 덮어쓰기
        pretrained=True,  # 사전 학습된 가중치 사용
        optimizer='auto',  # 최적화 알고리즘 자동 선택
        verbose=True,  # 상세 출력
        seed=42,  # 랜덤 시드
        patience=50,  # 조기 종료를 위한 인내심
    )

if __name__ == '__main__':
    main() 