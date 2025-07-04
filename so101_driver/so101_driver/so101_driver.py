from st3215 import ST3215


class SO101Driver:
    def __init__(self, port="/dev/ttyUSB0", speed=2400, accel=50):
        self.port = port
        self.speed = speed
        self.accel = accel

        self.servo = ST3215(port)

        self.mot_list = self.servo.ListServos()

    def detect(self):
        status = 0
        if self.mot_list:
            for id in self.mot_list:
                print("__________________________")
                print("                          ")
                print(f"Motor {id}")
                print(f"{self.read_status(id)=}")
            print("__________________________")
            status = 0
        else:
            status = 1
        return status

    def read_status(self, motor_id):
        return {
            "status": self.servo.ReadStatus(motor_id),
            "mode": self.servo.ReadMode(motor_id),
            "position": self.servo.ReadPosition(motor_id),
            "speed": self.servo.ReadSpeed(motor_id),
            "acceleration": self.servo.ReadAccelaration(motor_id),
        }

    def write_motor_pos(self, motor_id, position):
        status = self.servo.MoveTo(motor_id, position, self.speed, self.accel)
        return status

    def read_motor_pos(self, motor_id):
        return self.servo.ReadPosition(motor_id)
