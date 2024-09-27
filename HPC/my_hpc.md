---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---


# Slurm 集群配置指南

## 1. 硬件配置

### 1.1 控制节点 (zihancityu)

- CPUs: 20
- Memory: 125Gi
- GPUs: 3 x NVIDIA GeForce RTX 2080 Ti
- IP: 192.168.33.94

### 1.2 计算节点 (mercury)

- CPUs: 48
- Memory: 128Gi (根据配置文件)
- GPUs: 1 (类型未指定)
- IP: 192.168.33.34

## 2. 软件版本

- Slurm 版本: 23.11.4
- NVIDIA Driver 版本: 535.183.01
- CUDA 版本: 12.2

## 3. 配置文件

### 3.1 /etc/slurm/slurm.conf

```conf
SlurmctldHost=zihancityu
ClusterName=linuxcluster
GresTypes=gpu

SlurmctldPort=6817
SlurmdPort=6818

AuthType=auth/munge
StateSaveLocation=/var/spool/slurmd
SlurmdSpoolDir=/var/spool/slurmd
SlurmdLogFile=/var/log/slurm/slurmd.log
SwitchType=switch/none
MpiDefault=none
SlurmUser=slurm
SlurmdUser=root

# 节点定义
NodeName=zihancityu CPUs=20 Sockets=1 CoresPerSocket=20 Gres=gpu:3 RealMemory=128000 State=UNKNOWN
NodeName=mercury CPUs=48 Boards=1 SocketsPerBoard=2 CoresPerSocket=12 ThreadsPerCore=2 Gres=gpu:1 RealMemory=128000 State=UNKNOWN

# 分区定义
PartitionName=debug Nodes=zihancityu Default=YES MaxTime=INFINITE State=UP
PartitionName=cpu Nodes=mercury Default=NO MaxTime=INFINITE State=UP

CryptoType=crypto/munge
ReturnToService=1
SlurmctldPidFile=/var/run/slurmctld.pid
SlurmdPidFile=/var/run/slurmd.pid
ProctrackType=proctrack/cgroup
TaskPlugin=task/cgroup
```

### 3.2 /etc/slurm/gres.conf

```conf
# GPU 配置
NodeName=zihancityu Name=gpu File=/dev/nvidia0
NodeName=zihancityu Name=gpu File=/dev/nvidia1
NodeName=zihancityu Name=gpu File=/dev/nvidia2
```

### 3.2 /etc/hosts

```conf
127.0.0.1 localhost
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

192.168.33.34 mercury
192.168.33.94 zihancityu
```

## 4. 服务状态

### 4.1 slurmctld 服务 (在 zihancityu 上)

- 状态: active (running)
- 启动时间: Fri 2024-09-27 16:18:21 HKT

### 4.2 slurmd 服务 (在 zihancityu 上)

- 状态: active (running)
- 启动时间: Fri 2024-09-27 16:21:13 HKT

## 5. 故障排除

### 5.1 节点配置不匹配

在 zihancityu 上观察到以下警告：

```bash
slurmd: error: Node configuration differs from hardware: CPUs=20:20(hw) Boards=1:1(hw) SocketsPerBoard=1:1(hw) CoresPerSocket=20:10(hw) ThreadsPerCore=1:2(hw)
```

解决方法：调整 slurm.conf 中的节点配置以匹配实际硬件。例如：

```conf
NodeName=zihancityu CPUs=20 Sockets=1 CoresPerSocket=10 ThreadsPerCore=2 Gres=gpu:3 RealMemory=128000
```
