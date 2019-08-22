#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jansi
Version  : 1.17.1
Release  : 4
URL      : https://repo1.maven.org/maven2/org/fusesource/jansi/jansi/1.17.1/jansi-1.17.1.jar
Source0  : https://repo1.maven.org/maven2/org/fusesource/jansi/jansi/1.17.1/jansi-1.17.1.jar
Source1  : https://repo1.maven.org/maven2/org/fusesource/jansi/jansi-project/1.14/jansi-project-1.14.pom
Source2  : https://repo1.maven.org/maven2/org/fusesource/jansi/jansi-project/1.17.1/jansi-project-1.17.1.pom
Source3  : https://repo1.maven.org/maven2/org/fusesource/jansi/jansi/1.14/jansi-1.14.jar
Source4  : https://repo1.maven.org/maven2/org/fusesource/jansi/jansi/1.14/jansi-1.14.pom
Source5  : https://repo1.maven.org/maven2/org/fusesource/jansi/jansi/1.17.1/jansi-1.17.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-jansi-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-jansi package.
Group: Data

%description data
data components for the mvn-jansi package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/fusesource/jansi/jansi/1.17.1
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/fusesource/jansi/jansi/1.17.1/jansi-1.17.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/fusesource/jansi/jansi-project/1.14
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/fusesource/jansi/jansi-project/1.14/jansi-project-1.14.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/fusesource/jansi/jansi-project/1.17.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/fusesource/jansi/jansi-project/1.17.1/jansi-project-1.17.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/fusesource/jansi/jansi/1.14
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/fusesource/jansi/jansi/1.14/jansi-1.14.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/fusesource/jansi/jansi/1.14
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/fusesource/jansi/jansi/1.14/jansi-1.14.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/fusesource/jansi/jansi/1.17.1
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/fusesource/jansi/jansi/1.17.1/jansi-1.17.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/fusesource/jansi/jansi-project/1.14/jansi-project-1.14.pom
/usr/share/java/.m2/repository/org/fusesource/jansi/jansi-project/1.17.1/jansi-project-1.17.1.pom
/usr/share/java/.m2/repository/org/fusesource/jansi/jansi/1.14/jansi-1.14.jar
/usr/share/java/.m2/repository/org/fusesource/jansi/jansi/1.14/jansi-1.14.pom
/usr/share/java/.m2/repository/org/fusesource/jansi/jansi/1.17.1/jansi-1.17.1.jar
/usr/share/java/.m2/repository/org/fusesource/jansi/jansi/1.17.1/jansi-1.17.1.pom
