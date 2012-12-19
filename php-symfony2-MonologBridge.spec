%define		status		stable
%define		pearname	MonologBridge
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Symfony2 Monolog Bridge
Name:		php-symfony2-MonologBridge
Version:	2.1.4
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	eb83c017d553265e4feea86f32564c00
URL:		http://pear.symfony.com/package/MonologBridge/
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR >= 1:1.4.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php-channel(pear.symfony.com)
Requires:	php-pear >= 4:1.3.10
Requires:	php-symfony2-HttpKernel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Symfony2 Monolog Bridge

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

# no packaging of tests
rm -r .%{php_pear_dir}/Symfony/Bridge/Monolog/Tests
rm .%{php_pear_dir}/Symfony/Bridge/Monolog/phpunit.xml.dist

# fixups
mv .%{php_pear_dir}/Symfony/Bridge/Monolog/CHANGELOG.md .
rm .%{php_pear_dir}/Symfony/Bridge/Monolog/.gitattributes
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
%{php_pear_dir}/Symfony/Bridge/Monolog/Handler
%{php_pear_dir}/Symfony/Bridge/Monolog/Processor
