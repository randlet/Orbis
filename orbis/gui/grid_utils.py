#----------------------------------------------------------------------
def _set_number_of_rows_or_cols(getter,appender,deleter,desired_number):
    """add/remove rows to/from grid so that it's number of rows is same as input"""
    cur_number = getter()
    delta = cur_number - desired_number
    if delta > 0:
        deleter(0,min(cur_number,delta))
    elif delta < 0:
        appender(abs(delta))
    
#----------------------------------------------------------------------
def set_number_rows(grid,rows):
    """add/remove rows to/from grid so that it's number of rows is same as input"""
    _set_number_of_rows_or_cols(grid.GetNumberRows,grid.AppendRows,grid.DeleteRows,rows)
        
#----------------------------------------------------------------------
def set_number_cols(grid,cols):
    """add/remove rows to/from grid so that it's number of rows is same as input"""
    _set_number_of_rows_or_cols(grid.GetNumberCols,grid.AppendCols,grid.DeleteCols,cols)
#----------------------------------------------------------------------
def set_shape(grid,shape):
    """set number of rows and columns for grid to shape=(rows,cols)"""
    set_number_rows(grid,shape[0])    
    set_number_cols(grid,shape[1])
#----------------------------------------------------------------------
def get_shape(grid):
    """return current shape of grid"""
    return (grid.GetNumberRows(),grid.GetNumberCols())
    