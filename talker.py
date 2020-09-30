import time

import roslibpy

client = roslibpy.Ros(host='192.168.1.180', port=9090)
client.run()

gpsgoal = roslibpy.Topic(client, '/gps_goal_fix', 'sensor_msgs/NavSatFix')
gpspose = roslibpy.Topic(client, '/gps_goal_pose', 'geometry_msgs/PoseStamped')

while client.is_connected:
    gpsgoal.publish(roslibpy.Message({'latitude': 38.42, 'longitude': -110.79}))
    gpspose.publish(roslibpy.Message({ 'header': { 'frame_id': '/map' }, 'pose': { 'position': { 'x': 43.658, 'y': -79.379 } } }))
    print('Sending message...')
    
    time.sleep(1)

talker.unadvertise()

client.terminate()
