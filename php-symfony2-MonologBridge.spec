%define		package	MonologBridge
%define		php_min_version 5.3.9
Summary:	Symfony2 Monolog Bridge
Name:		php-symfony2-MonologBridge
Version:	2.8.52
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	e625fa0071fe2e1de48bad8c307d63c0
URL:		https://github.com/symfony/MonologBridge
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-dirs >= 1.6
#Requires:	php-monolog-Monolog >= 1.11
Suggests:	php-symfony2-Console >= 2.3
Suggests:	php-symfony2-EventDispatcher
Suggests:	php-symfony2-HttpKernel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides integration for Monolog with various Symfony2 components.

%prep
%setup -q -n monolog-bridge-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Bridge/Monolog
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Bridge/Monolog
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Bridge/Monolog/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_data_dir}/Symfony/Bridge/Monolog
%{php_data_dir}/Symfony/Bridge/Monolog/*.php
%{php_data_dir}/Symfony/Bridge/Monolog/Formatter
%{php_data_dir}/Symfony/Bridge/Monolog/Handler
%{php_data_dir}/Symfony/Bridge/Monolog/Processor
