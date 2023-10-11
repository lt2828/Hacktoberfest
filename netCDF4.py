import netCDF4 as nc
import numpy as np

# Open an existing netCDF file for reading
data = nc.Dataset('your_existing_file.nc', 'r')

# Access a variable
variable = data.variables['variable_name']

# Read the data from the variable
variable_data = variable[:]

# Access an attribute of the variable
attribute_value = variable.getncattr('attribute_name')

# Close the existing netCDF file
data.close()

# Create a new netCDF file for writing
new_data = nc.Dataset('new_file.nc', 'w')

# Create a new variable, assign data to it, and set attributes
new_variable = new_data.createVariable('new_variable_name', 'f4', ('dimension_name',))
new_data_description = "This is a new variable in a new netCDF file."
new_variable.description = new_data_description
new_variable[:] = np.arange(10)  # Example data

# Close the new netCDF file
new_data.close()
