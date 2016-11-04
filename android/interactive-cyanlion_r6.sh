# Script Author: Austin Haedicke (gtbjj @ github)
#
# Settings by xSilas43
# https://androidfilehost.com/?fid=24391638059060083

CPU0=/sys/devices/system/cpu/cpu0/cpufreq/interactive
CPU4=/sys/devices/system/cpu/cpu4/cpufreq/interactive

# change permissions and set governor
chmod 644 $CPU0/cpu_freq/scaling_governor
echo interactive > $CPU0/cpu_freq/scaling_governor
chmod 444 $CPU0/cpu_freq/scaling_governor
echo 1 > $CPU4/online
chmod 644 $CPU4/cpufreq/scaling_governor
echo interactive > $CPU4/cpu_freq/scaling_governor
chmod 444 $CPU4/cpu_freq/scaling_governor

# apply settings to LITTLE cluster
echo 99 > $CPU0/go_hispeed_load
echo 50000 672000:60000 864000:20000 > $CPU0/above_hispeed_delay 
echo 50000 > $CPU0/timer_rate
echo 384000 > $CPU0/cpufreq/interactive/hispeed_freq 
echo 80000 > $CPU0/cpufreq/interactive/timer_slack
echo 98 384000:75 460000:30 600000:12 672000:14 768000:80 864000:11 960000:69 1248000:8 1344000:82 1478000:99 1555000:99 > $CPU0/cpufreq/interactive/target_loads
echo 80000 > $CPU0/cpufreq/interactive/min_sample_time
echo 0 > $CPU0/cpufreq/interactive/align_windows
echo 1 > $CPU0/cpufreq/interactive/use_migration_notif
echo 0 > $CPU0/cpufreq/interactive/use_sched_load
echo 80000 > $CPU0/cpufreq/interactive/max_freq_hysteresis
echo 80000 > $CPU0/cpufreq/interactive/boostpulse_duration

# apply settings to Big cluster
echo 99 > $CPU4/cpufreq/interactive/go_hispeed_load
echo 40000 > $CPU4/cpufreq/interactive/above_hispeed_delay
echo 50000 > $CPU4/cpufreq/interactive/timer_rate
echo 1958400 > $CPU4/cpufreq/interactive/hispeed_freq
echo 80000 > $CPU4/cpufreq/interactive/timer_slack
echo 98 633000:74 768000:13 864000:11 960000:3 1248000:8 1344000:7 1440000:6 1536000:87 1632000:6 1728000:5 1824000:7 1958400:99 > $CPU4/cpufreq/interactive/target_loads 
echo 70000 > $CPU4/cpufreq/interactive/min_sample_time
echo 0 > $CPU4/cpufreq/interactive/align_windows
echo 1 > $CPU4/cpufreq/interactive/use_migration_notif
echo 0 > $CPU4/cpufreq/interactive/use_sched_load
echo 80000 > $CPU4/cpufreq/interactive/max_freq_hysteresis
echo 80000 > $CPU4/cpufreq/interactive/boostpulse_duration

# disabling touch and input boost
/sys/module/cpu_boost/parameters/input_boost_freq 0:0 1:0 2:0 3:0 4:0 5:0 6:0 7:0
/sys/module/cpu_boost/parameters/boost_ms 0
/sys/module/cpu_boost/parameters/input_boost_ms 0
/sys/module/msm_performance/parameters/touchboost 0

echo "Settings Successfully Applied!"
