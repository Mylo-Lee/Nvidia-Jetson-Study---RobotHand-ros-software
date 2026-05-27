# Jetson-Free ROS 1 다관절 로봇 손 제어 프레임워크

본 프로젝트는 실제 하드웨어 없이 ROS 1 환경에서 다관절 로봇 손의 통신 무결성 및 제어 파이프라인을 검증하기 위한 가상 환경 프레임워크입니다.

## 요구 사항
- Ubuntu (또는 WSL2 환경)
- ROS 1 Noetic
- Python 3
- OpenCV (`cv_bridge`)

## 빌드 방법 (Build Instructions)
1. 워크스페이스 디렉토리로 이동합니다.
   ```bash
   cd ~/catkin_ws
   ```
2. 패키지를 빌드합니다.
   ```bash
   catkin_make
   ```
3. 환경 변수를 로드합니다.
   ```bash
   source devel/setup.bash
   ```

## 실행 방법 (How to Run)
본 시스템은 가상 카메라 뷰어, 궤적 연산, 가상 구동부 등 여러 노드로 구성되어 있습니다. 사용자 입력을 받기 위해 터미널을 분리하여 실행하는 것을 권장합니다.

**터미널 1: 코어 노드 전체 실행**
```bash
roslaunch dexterous_hand_core dexterous_hand.launch
```

**터미널 2: 이미지 뷰어 실행 (선택 사항)**
가상 카메라가 송출하는 화면("카메라 실행중")을 봅니다.
```bash
rosrun rqt_image_view rqt_image_view
```
> 좌상단 드롭다운에서 `/camera/image_raw`를 선택하세요.

**터미널 3: 키보드 입력(Teleop) 노드 실행**
사용자의 키보드 입력을 받아 로봇 손을 제어합니다. (반드시 이 터미널을 활성화한 상태에서 키를 입력하세요.)
```bash
rosrun dexterous_hand_core teleop_input_node.py
```

## 단축키 조작 가이드 (Shortcut Keys)
`teleop_input_node.py`가 실행된 터미널 창을 선택한 후, 아래 키보드를 누르면 15개 관절이 일제히 동작하며 `터미널 1`의 로그에 결과가 출력됩니다.

| 키보드 | 동작 이름 | 설명 |
| :---: | :--- | :--- |
| **q** | **Open Hand** | 15개 관절을 0도로 초기화하여 손을 활짝 폅니다. |
| **w** | **Close Hand** | 주먹을 쥡니다. (모든 관절 1.57 라디안 굽힘) |
| **e** | **Pinch** | 꼬집기. (엄지와 검지만 구부림) |
| **r** | **Point** | 가리키기. (검지만 펴고 나머지는 주먹) |
| **s** | **Stop / Reset** | 즉시 초기 상태로 리셋합니다. |
| **CTRL-C** | **Quit** | 노드를 종료합니다. |

## 메시지 흐름
1. `teleop_input_node` ➔ `/teleop/keyboard_cmd` 발행
2. `main_planning_node` ➔ 명령 분석 후 관절 궤적 연산 ➔ `/planning/target_joints` 발행
3. `hand_actuator_node` ➔ `/planning/target_joints` 구독 후 실시간 출력(가상 구동 확인)
