from netmiko import ConnectHandler
## Define our new function called bootstrapper and the expected arguments (all five)
def bootstrapper(dev_type, dev_ip, dev_un, dev_pw, config):
    try:
        config_file = open(config, "r") # open the file object described by config argument
        config_lines = config_file.read().splitlines() # create a list of the file lines without \n
        config_file.close() # close the file

        open_connection = ConnectHandler(device_type=dev_type, ip=dev_ip, username=dev_un, password=dev_pw)
        open_connection.enable() # this sets the connection in enable mode
        # pass the config to the send_config_set() method
        output = open_connection.send_config_set(config_lines)
        print(output)
        open_connection.send_command_expect('write_memory') # write the memory (okay if this gets done twice)
        open_connection.disconnect() # closes the connection

        return True # If everything worked, it'll return True
    except:
        return False # If something went wrong, return False

