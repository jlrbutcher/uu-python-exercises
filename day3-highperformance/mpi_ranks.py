from mpi4py import MPI

def main():
    # Get the global communicator (all processes)
    comm = MPI.COMM_WORLD
    
    # Get the rank of the current process
    # (The ID number of this specific instance)
    rank = comm.Get_rank()
    
    # Get the total number of processes
    size = comm.Get_size()
    
    print(f"Hello! I am process {rank} of {size} total processes.")

if __name__ == "__main__":
    main()
