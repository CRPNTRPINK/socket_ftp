from file_manager import FileManager


def manager(command, path, file_manager):
    if file_manager.get_pathway() is False:
        file_manager.set_pathway(path)
    try:
        command = command.split(' ')
        if command[0] == 'pwd':
            return file_manager.get_pwd()

        elif command[0] + command[1] == 'getlist':
            if len(command) == 2:
                return file_manager.show_list()
            else:
                return file_manager.show_list(command[2])

        elif (command[0] + command[1]) == 'moveup':
            return file_manager.move_up()

        elif (command[0] + command[1]) == 'create-d':
            return file_manager.create_directory(command[2])

        elif (command[0] + command[1]) == 'remove-d':
            return file_manager.remove_directory(command[2])

        elif (command[0] + command[1]) == 'movein':
            return file_manager.move_in_path(command[2])

        elif (command[0] + command[1]) == 'create-f':
            return file_manager.create_file(command[2])

        elif (command[0] + command[1]) == 'read-f':
            return file_manager.read_file(command[2])

        elif (command[0] + command[1]) == 'remove-f':
            return file_manager.delete_file(command[2])

        elif (command[0] + command[1]) == 'copy-f':
            return file_manager.copy_file(command[2], command[3])

        elif (command[0] + command[1]) == 'move-f':
            return file_manager.move_file(command[2], command[3])

        elif (command[0] + command[1]) == 'rename-f':
            return file_manager.rename_file(command[2], command[3])

        elif (command[0] + command[1]) == 'write-f':
            return file_manager.write_file(command[2], ' '.join(command[3:]))

        elif (command[0] + command[1]) == 'download-s':
            return file_manager.download_file(command[2], command[3])

        elif (command[0] + command[1]) == 'download-c':
            return file_manager.send_file(command[2], command[3])

        else:
            return 'Команда введена неверно'
    except IndexError:
        return 'Команда введена неверно'
