---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---
# Openmp and MPI
- OpenMP is a shared memory parallel programming model.
- MPI is a distributed memory parallel programming model.
## Rust Libraries
- [mpi](https://docs.rs/mpi/latest/mpi/) can be used to convey messages between processes.
## MPI Example
```c
#include <mpi.h>
#include <stdio.h>
int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);
    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    int n = 10; // 总元素数量
    int local_n = n / size; // 每个进程处理的元素数量
    int local_sum = 0, total_sum = 0;
    int a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    // 每个进程计算部分和
    for (int i = rank * local_n; i < (rank + 1) * local_n; i++) {
        local_sum += a[i];
    }
    // 将所有局部和汇总到总和中
    MPI_Reduce(&local_sum, &total_sum, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
    if (rank == 0) {
        printf("Total sum = %d\n", total_sum);
    }
    MPI_Finalize();
    return 0;
}
```
```bash
mpicc mpi_example.c -o mpi_example
mpirun -np 4 ./mpi_example
```
## OpenMP Example
```c
#include <omp.h>
#include <stdio.h>
int main() {
    int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int sum = 0;
    int n = 10;
    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < n; i++) {
        sum += a[i];
    }
    printf("Sum = %d\n", sum);
    return 0;
}
```
```bash
gcc -fopenmp openmp_example.c -o openmp_example
./openmp_example
```
