%{?scl:%scl_package nodejs-columnify}
%{!?scl:%global pkg_name %{name}}

%global npmname columnify
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-columnify
Version:        1.3.2
Release:        5%{?dist}
Summary:        Render data in text columns, supports in-column text-wrap.
Url:            https://github.com/timoxley/columnify
Source0:        http://registry.npmjs.org/columnify/-/columnify-%{version}.tgz
License:        MIT

BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Render data in text columns, supports in-column text-wrap.

%prep
%setup -q -n package

%nodejs_fixdep strip-ansi '>= 3.0.0'

%build
#nothing to do

%install
rm -rf %buildroot

mkdir -p %{buildroot}%{nodejs_sitelib}/columnify
cp -pr index.js utils.js width.js  package.json %{buildroot}%{nodejs_sitelib}/columnify

%nodejs_symlink_deps

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/columnify

%doc Readme.md

%changelog
* Tue Feb 16 2016 Tomas Hrcka <thrcka@redhat.com> - 1.3.2-5
- Fix dependency on strip-ansi 

* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 1.3.2-3
- New upstream release 1.3.2

* Mon Feb 17 2014 Tomas Hrcka <thrcka@redhat.com> - 0.1.2-1
- Initial build 

