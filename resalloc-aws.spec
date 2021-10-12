%global srcname resalloc-aws

Name:       resalloc-aws
Summary:    Resource allocator scripts for AWS
Version:    1
Release:    1%{?dist}
License:    GPLv2+
URL:        https://github.com/praiskup/resalloc-aws
BuildArch:  noarch

Requires: awscli

# Source is created by:
# git clone %%url && cd copr
# tito build --tgz --tag %%name-%%version-%%release
Source0: %{name}-%{version}.tar.gz

# This one is bundled, though it is GPLv2+, too.
Source1: https://raw.githubusercontent.com/praiskup/wait-for-ssh/main/wait-for-ssh


%description
When allocating/removing machine in AWS/EC2 from command-line, there are many
non-trivial options in the 'aws-cli' command.  This project provides a
simplified wrapping command.

The 'resalloc-aws-new' script is able to (a) start the machine, (b) wait till
SSH is available and (c) run a specified playbook.

The 'resalloc-aws-delete' removes the machine started by 'resalloc-aws-new'
script.

These scripts are primarily designed to be used with 'resalloc-server', but they
might be used separately.


%prep
%setup -q


%install
mkdir -p %buildroot%_bindir
install -p -m 0755 bin/resalloc-aws-new %buildroot/%_bindir
install -p -m 0755 bin/resalloc-aws-delete %buildroot/%_bindir
install -p -m 0755 %SOURCE1 %buildroot/%_bindir/resalloc-aws-wait-for-ssh
sed '1c#! /usr/bin/python3' -i %buildroot/%_bindir/resalloc-aws-wait-for-ssh


%files
%license COPYING
%doc README.md
%{_bindir}/%{name}-*


%changelog
* Tue Oct 12 2021 Pavel Raiskup <praiskup@redhat.com> 1-1
- new package built with tito
