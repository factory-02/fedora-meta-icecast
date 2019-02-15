Name:                           meta-icecast
Version:                        1.0.1
Release:                        1%{?dist}
Summary:                        META-package for install and configure Icecast
License:                        GPLv3

Source10:                       icecast.xml

Requires:                       icecast

%description
META-package for install and configure Icecast.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%install
%{__mkdir} -p %{buildroot}%{_sysconfdir}
install -p -m 0644 %{SOURCE10} \
    %{buildroot}%{_sysconfdir}/icecast.xml

%files
%config %{_sysconfdir}/icecast.xml

%changelog
* Fri Feb 15 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.1-1
- New version: 1.0.1.

* Fri Feb 15 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.0-1
- Initial build.
