import board
import digitalio
import storage

# TODO: Which pin is this?
#toggle = digitalio.DigitalInOut(board.D5)

#toggle.direction = digitalio.Direction.INPUT
#toggle.pull = digitalio.Pull.UP

# If the toggle pin is connected to ground, then CircuitPython can write to the drive
# If not, then CircuitPython cannot, so a plugged-in computer can instead.
#storage.remount("/", toggle.value)

# Until I find the right pin to use, we'll do this madness...

print("* * * * * * * * * * * * * * * * * * * * * * * * * * ")
print("File system is disabling concurrent write protection")
print("               Back. Up. Everything.")
print("* * * * * * * * * * * * * * * * * * * * * * * * * * ")
storage.remount("/", disable_concurrent_write_protection=True)
