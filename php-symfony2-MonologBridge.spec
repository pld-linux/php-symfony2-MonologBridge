%define		pearname	MonologBridge
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Monolog Bridge
Name:		php-symfony2-MonologBridge
Version:	2.4.3
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	f1ad941993a478765503015c4d6d8831
URL:		https://github.com/symfony/MonologBridge
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR >= 1:1.4.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-channel(pear.symfony.com)
#Requires:	php-monolog-Monolog >= 1.3
Requires:	php-pear >= 4:1.3.10
Suggests:	php-symfony2-Console >= 2.3
Suggests:	php-symfony2-EventDispatcher
Suggests:	php-symfony2-HttpKernel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides integration for Monolog with various Symfony2 components.

%prep
%pear_package_setup

# no packaging of tests
mv .%{php_pear_dir}/Symfony/Bridge/Monolog/Tests .
mv .%{php_pear_dir}/Symfony/Bridge/Monolog/phpunit.xml.dist .

# fixups
mv docs/%{pearname}/Symfony/Bridge/Monolog/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/Symfony/Bridge/Monolog
%{php_pear_dir}/Symfony/Bridge/Monolog/*.php
%{php_pear_dir}/Symfony/Bridge/Monolog/Formatter
%{php_pear_dir}/Symfony/Bridge/Monolog/Handler
%{php_pear_dir}/Symfony/Bridge/Monolog/Processor
