from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_rsp_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("so101_new_calib", package_name="so101_moveit_description").to_moveit_configs()
    return generate_rsp_launch(moveit_config)
