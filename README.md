Allocate machine in AWS
=======================

When allocating/removing machine in AWS/EC2 from command-line, there are many
non-trivial options in the 'aws-cli' command.  This project provides a
simplified variant.

The 'resalloc-aws-new' script is able to (a) start the machine, (b) wait till
SSH is available and (c) run a specified playbook.

The 'resalloc-aws-delete' removes the machine started by 'resalloc-aws-new'
script.

API
===

The scripts provide the compatible API with closely related to Resalloc [1]
project:

- The '*-new' script either succeeds (provides the specified, configured, and
  fully working machine) or fails (and all the byproducts are cleaned-up from
  EC2).
- Upon '*-new' success, the IP address of the machine is printed to stdout.
- The '*-delete' script does it's best to remove the selected machine, even
  repetitively (to avoid paying for unused resources).

References
----------

[1] https://github.com/praiskup/resalloc
