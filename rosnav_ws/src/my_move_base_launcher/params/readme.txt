/amcl/gui_publish_rate: 10.0
 * /amcl/kld_err: 0.05
 * /amcl/kld_z: 0.99
 * /amcl/laser_lambda_short: 0.1
 * /amcl/laser_likelihood_max_dist: 2.0
 * /amcl/laser_max_beams: 60
 * /amcl/laser_max_range: 12.0
 * /amcl/laser_model_type: likelihood_field
 * /amcl/laser_sigma_hit: 0.2
 * /amcl/laser_z_hit: 0.5
 * /amcl/laser_z_max: 0.05
 * /amcl/laser_z_rand: 0.5
 * /amcl/laser_z_short: 0.05
 * /amcl/max_particles: 2000
 * /amcl/min_particles: 500
 * /amcl/odom_alpha1: 0.2
 * /amcl/odom_alpha2: 0.2
 * /amcl/odom_alpha3: 0.2
 * /amcl/odom_alpha4: 0.2
 * /amcl/odom_alpha5: 0.1
 * /amcl/odom_frame_id: odom
 * /amcl/odom_model_type: diff
 * /amcl/recovery_alpha_fast: 0.0
 * /amcl/recovery_alpha_slow: 0.0
 * /amcl/resample_interval: 1
 * /amcl/transform_tolerance: 1.0
 * /amcl/update_min_a: 0.2
 * /amcl/update_min_d: 0.25
 * /amcl/use_map_topic: True
 * /move_base/DWAPlannerROS/acc_lim_th: 3.2
 * /move_base/DWAPlannerROS/acc_lim_x: 2.5
 * /move_base/DWAPlannerROS/acc_lim_y: 0
 * /move_base/DWAPlannerROS/latch_xy_goal_tolerance: False
 * /move_base/DWAPlannerROS/max_rot_vel: 1.0
 * /move_base/DWAPlannerROS/max_trans_vel: 0.5
 * /move_base/DWAPlannerROS/max_vel_x: 0.5
 * /move_base/DWAPlannerROS/max_vel_y: 0
 * /move_base/DWAPlannerROS/min_rot_vel: 0.2
 * /move_base/DWAPlannerROS/min_trans_vel: 0.1
 * /move_base/DWAPlannerROS/min_vel_x: 0.0
 * /move_base/DWAPlannerROS/min_vel_y: 0
 * /move_base/DWAPlannerROS/xy_goal_tolerance: 0.2
 * /move_base/DWAPlannerROS/yaw_goal_tolerance: 0.1
 * /move_base/NavfnROS/allow_unknown: True
 * /move_base/NavfnROS/default_tolerance: 0.1
 * /move_base/NavfnROS/use_dijkstra: False
 * /move_base/TrajectoryPlannerROS/acc_lim_theta: 3.2
 * /move_base/TrajectoryPlannerROS/acc_lim_x: 2.5
 * /move_base/TrajectoryPlannerROS/angular_sim_granularity: 0.02
 * /move_base/TrajectoryPlannerROS/controller_frequency: 20.0
 * /move_base/TrajectoryPlannerROS/dwa: True
 * /move_base/TrajectoryPlannerROS/escape_reset_dist: 0.1
 * /move_base/TrajectoryPlannerROS/escape_reset_theta: 0.1
 * /move_base/TrajectoryPlannerROS/escape_vel: -0.1
 * /move_base/TrajectoryPlannerROS/gdist_scale: 1.0
 * /move_base/TrajectoryPlannerROS/heading_lookahead: 0.325
 * /move_base/TrajectoryPlannerROS/heading_scoring: False
 * /move_base/TrajectoryPlannerROS/heading_scoring_timestep: 0.8
 * /move_base/TrajectoryPlannerROS/holonomic_robot: False
 * /move_base/TrajectoryPlannerROS/latch_xy_goal_tolerance: False
 * /move_base/TrajectoryPlannerROS/max_vel_theta: 1.0
 * /move_base/TrajectoryPlannerROS/max_vel_x: 1.0
 * /move_base/TrajectoryPlannerROS/meter_scoring: True
 * /move_base/TrajectoryPlannerROS/min_in_place_vel_theta: 0.2
 * /move_base/TrajectoryPlannerROS/min_vel_theta: -1.0
 * /move_base/TrajectoryPlannerROS/min_vel_x: 0.0
 * /move_base/TrajectoryPlannerROS/occdist_scale: 0.1
 * /move_base/TrajectoryPlannerROS/oscillation_reset_dist: 0.25
 * /move_base/TrajectoryPlannerROS/pdist_scale: 0.75
 * /move_base/TrajectoryPlannerROS/publish_cost_grid_pc: True
 * /move_base/TrajectoryPlannerROS/sim_granularity: 0.02
 * /move_base/TrajectoryPlannerROS/sim_time: 2.0
 * /move_base/TrajectoryPlannerROS/simple_attractor: False
 * /move_base/TrajectoryPlannerROS/vtheta_samples: 20
 * /move_base/TrajectoryPlannerROS/vx_samples: 6
 * /move_base/TrajectoryPlannerROS/xy_goal_tolerance: 0.7
 * /move_base/TrajectoryPlannerROS/yaw_goal_tolerance: 0.5
 * /move_base/base_global_planner: navfn/NavfnROS
 * /move_base/base_local_planner: dwa_local_planner...
 * /move_base/controller_frequency: 5.0
 * /move_base/global_costmap/footprint: [[-0.5, -0.33], [...
 * /move_base/global_costmap/footprint_padding: 0.01
 * /move_base/global_costmap/global_frame: map
 * /move_base/global_costmap/inflation/inflation_radius: 1.0
 * /move_base/global_costmap/obstacle_range: 5.5
 * /move_base/global_costmap/obstacles_laser/laser/clearing: True
 * /move_base/global_costmap/obstacles_laser/laser/data_type: LaserScan
 * /move_base/global_costmap/obstacles_laser/laser/inf_is_valid: True
 * /move_base/global_costmap/obstacles_laser/laser/marking: True
 * /move_base/global_costmap/obstacles_laser/laser/topic: scan
 * /move_base/global_costmap/obstacles_laser/observation_sources: laser
 * /move_base/global_costmap/plugins: [{'type': 'costma...
 * /move_base/global_costmap/publish_frequency: 3.0
 * /move_base/global_costmap/raytrace_range: 6.0
 * /move_base/global_costmap/resolution: 0.05
 * /move_base/global_costmap/robot_base_frame: base_link
 * /move_base/global_costmap/rolling_window: False
 * /move_base/global_costmap/static/map_topic: /map
 * /move_base/global_costmap/static/subscribe_to_updates: True
 * /move_base/global_costmap/track_unknown_space: True
 * /move_base/global_costmap/transform_tolerance: 0.5
 * /move_base/global_costmap/update_frequency: 4.0
 * /move_base/local_costmap/footprint: [[-0.5, -0.33], [...
 * /move_base/local_costmap/footprint_padding: 0.01
 * /move_base/local_costmap/global_frame: odom
 * /move_base/local_costmap/height: 5.0
 * /move_base/local_costmap/inflation/inflation_radius: 1.0
 * /move_base/local_costmap/obstacle_range: 5.5
 * /move_base/local_costmap/obstacles_laser/laser/clearing: True
 * /move_base/local_costmap/obstacles_laser/laser/data_type: LaserScan
 * /move_base/local_costmap/obstacles_laser/laser/inf_is_valid: True
 * /move_base/local_costmap/obstacles_laser/laser/marking: True
 * /move_base/local_costmap/obstacles_laser/laser/topic: scan
 * /move_base/local_costmap/obstacles_laser/observation_sources: laser
 * /move_base/local_costmap/plugins: [{'type': 'costma...
 * /move_base/local_costmap/publish_frequency: 3.0
 * /move_base/local_costmap/raytrace_range: 6.0
 * /move_base/local_costmap/resolution: 0.05
 * /move_base/local_costmap/robot_base_frame: base_link
 * /move_base/local_costmap/rolling_window: True
 * /move_base/local_costmap/static/map_topic: /map
 * /move_base/local_costmap/static/subscribe_to_updates: True
 * /move_base/local_costmap/transform_tolerance: 0.5
 * /move_base/local_costmap/update_frequency: 5.0
 * /move_base/local_costmap/width: 5.0
 * /move_base/recovery_behaviour_enabled: True
 * /rosdistro: kinetic
 * /rosversion: 1.12.14

NODES
  /
    amcl (amcl/amcl)
    map_server (map_server/map_server)
    move_base (move_base/move_base)

ROS_MASTER_URI=http://10.8.0.1:11311

process[map_server-1]: started with pid [1649]
process[amcl-2]: started with pid [1652]
process[move_base-3]: started with pid [1695]
[ INFO] [1543507553.423455219, 2286.810000000]: Using plugin "static"
[ INFO] [1543507553.526701065, 2286.865000000]: Requesting the map...
[ INFO] [1543507553.743587292, 2287.004000000]: Resizing costmap to 608 X 608 at 0.050000 m/pix
[ INFO] [1543507553.917372452, 2287.104000000]: Received a 608 X 608 map at 0.050000 m/pix
[ INFO] [1543507553.917421466, 2287.104000000]: Subscribing to updates
[ INFO] [1543507554.059245063, 2287.186000000]: Using plugin "obstacles_laser"
[ INFO] [1543507554.116041116, 2287.222000000]:     Subscribed to Topics: laser
[ INFO] [1543507554.572873905, 2287.534000000]: Using plugin "inflation"
[ INFO] [1543507555.670915814, 2288.208000000]: Using plugin "obstacles_laser"
[ INFO] [1543507555.721232849, 2288.237000000]:     Subscribed to Topics: laser
[ INFO] [1543507556.268973972, 2288.546000000]: Using plugin "inflation"
[ INFO] [1543507557.351797340, 2289.172000000]: Created local_planner dwa_local_planner/DWAPlannerROS
[ INFO] [1543507557.438706816, 2289.219000000]: Sim period is set to 0.20
[ INFO] [1543507559.737561918, 2290.672000000]: Recovery behavior will clear layer obstacles
[ INFO] [1543507559.793316532, 2290.706000000]: Recovery behavior will clear layer obstacles
