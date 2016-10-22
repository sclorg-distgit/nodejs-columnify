%{?scl:%scl_package nodejs-columnify}
%{!?scl:%global pkg_name %{name}}

%global npmname columnify
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-columnify
Version:        1.5.4
Release:        1%{?dist}
Summary:        Render data in text columns, supports in-column text-wrap.
Url:            https://github.com/timoxley/columnify
Source0:        http://registry.npmjs.org/columnify/-/columnify-%{version}.tgz
License:        MIT
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch
BuildArch:	    noarch
BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Render data in text columns, supports in-column text-wrap.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot

mkdir -p %{buildroot}%{nodejs_sitelib}/columnify
cp -pr index.js utils.js width.js columnify.js  package.json %{buildroot}%{nodejs_sitelib}/columnify

%nodejs_symlink_deps

%clean
rm -rf %buildroot

%files
%{nodejs_sitelib}/columnify
%doc LICENSE
%doc Readme.md

%changelog
* Thu Apr 07 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.5.4-1
- Update to 1.5.4

* Tue Feb 16 2016 Tomas Hrcka <thrcka@redhat.com> - 1.3.2-5
- Fix dependency on strip-ansi 

* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 1.3.2-3
- New upstream release 1.3.2

* Mon Feb 17 2014 Tomas Hrcka <thrcka@redhat.com> - 0.1.2-1
- Initial build 

