# TODO:
# - javadoc package
Summary:	A diagram editing framework
Summary(pl.UTF-8):	Szkielet do edycji diagramów
Name:		gef
Version:	0.10.7
Release:	0.1
License:	Apache License
Group:		Development/Languages/Java
Source0:	http://gef.tigris.org/files/documents/9/10445/GEF-%{version}-src.zip
# Source0-md5:	bb4c1f5e902bbe9ad882794e88994e4c
URL:		http://gef.tigris.org/
BuildRequires:	ant
BuildRequires:	jakarta-commons-logging
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	jakarta-log4j
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of the GEF project is to build a graph editing library that
can be used to construct many, high-quality graph editing
applications. Some of GEF's features are:
- A simple, concrete design that makes the framework easy to
  understand and extend.
- Node-Port-Edge graph model that is powerful enough for the vast
  majority of connected graph applications.
- Model-View-Controller design based on the Swing Java UI library
  makes GEF able to act as a UI to existing data structures, and also
  minimizing learning time for developers familiar with Swing.
- High-quality user interactions for moving, resizing, reshaping,
  etc. GEF also supports several novel interactions such as the broom
  alignment tool and section-action-buttons.
- Generic properties sheet based on JavaBeans introspection.
- XML-based file formats based on the PGML standard (soon to support
  SVG).

%description -l pl.UTF-8
Celem projektu GEF jest stworzenie biblioteki do edycji grafów, której
można używać do konstruowania wielu wysokiej jakości aplikacji do
edycji grafów. Niektóre możliwości pakietu GEF to:
- prosty, konkretny projekt czyniący środowisko łatwym do zrozumienia
  i rozszerzania
- model grafów wierzchołek-port-krawędź wystarczający do przeważającej
  większości zastosowań trafów
- projekt model-widok-kontroler oparty na bibliotece UI Javy Swing,
  dzięki któremu pakiet GEF może działać jako interfejs użytkownika do
  istniejących struktur danych, a także minimalizujący czas nauki dla
  programistów znających Swinga
- wysokiej jakości interakcja z użytkownikiem przy przesuwaniu,
  zmianie rozmiaru, kształtu itp.; GEF obsługuje także różne nowe
  interakcje, takie jak "miotłę" (narzędzie do wyrównywania) oraz
  przyciski sekcji-akcji
- arkusz ogólnych własności oparty na introspekcji JavaBeans
- formaty plików XML oparte na standardzie PGML (wkrótce obsługa SVG).

%package doc
Summary:	Javadoc for %{name}
Summary(pl.UTF-8):	Dokumentacja Javadoc dla %{name}
Group:		Documentation

%description doc
Javadoc for %{name}.

%description doc -l pl.UTF-8
Dokumentacja Javadoc dla %{name}.

%prep
%setup -q -c -T
mkdir src
cd src
unzip -q %{SOURCE0}
# remove binary files
find -name '*.jar' | xargs rm -v

%build
%ant package

%install
rm -rf $RPM_BUILD_ROOT
install -D lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc src/COPYRIGHT src/INSTALL.txt src/readme.txt
%{_javadir}/*.jar
