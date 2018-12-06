# https://github.com/cespare/xxhash
%global goipath         github.com/cespare/xxhash
Version:                1.1.0

%gometa

Name:           %{goname}
Release:        0.1%{?dist}
Summary:        A Go implementation of the 64-bit xxHash algorithm (XXH64)
# Detected licences
# - Expat License at 'LICENSE.txt'
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}


%description
%{summary}


%package devel
Summary:       %{summary}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE.txt
%doc README.md


%changelog
* Sat Nov 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-1
- Release 1.1.0
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 13 2018 Kaushal <kshlmster@gmail.com> - 1.0.0-1
- First package for Fedora
