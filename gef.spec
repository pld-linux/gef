# TODO:
# javadoc package
Summary:	A diagram editing framework
Summary(pl):	Szkielet do edycji diagramów
Name:		gef
Version:	0.10.7
Release:	0.1
License:	Apache License
Group:		Development/Languages/Java
Source0:	http://gef.tigris.org/files/documents/9/10445/GEF-%{version}-src.zip
# Source0-md5:	bb4c1f5e902bbe9ad882794e88994e4c
URL:		http://gef.tigris.org/
BuildRequires:	jakarta-ant
BuildRequires:	jakarta-commons-logging
Requires:	jakarta-log4j
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

%description -l pl
Celem projektu GEF jest stworzenie biblioteki do edycji grafów, której
mo¿na u¿ywaæ do konstruowania wielu wysokiej jako¶ci aplikacji do
edycji grafów. Niektóre mo¿liwo¶ci pakietu GEF to:
- prosty, konkretny projekt czyni±cy ¶rodowisko ³atwym do zrozumienia
  i rozszerzania
- model grafów wierzcho³ek-port-krawêd¼ wystarczaj±cy do przewa¿aj±cej
  wiêkszo¶ci zastosowañ trafów
- projekt model-widok-kontroler oparty na bibliotece UI Javy Swing,
  dziêki któremu pakiet GEF mo¿e dzia³aæ jako interfejs u¿ytkownika do
  istniej±cych struktur danych, a tak¿e minimalizuj±cy czas nauki dla
  programistów znaj±cych Swinga
- wysokiej jako¶ci interakcja z u¿ytkownikiem przy przesuwaniu,
  zmianie rozmiaru, kszta³tu itp.; GEF obs³uguje tak¿e ró¿ne nowe
  interakcje, takie jak "miot³ê" (narzêdzie do wyrównywania) oraz
  przyciski sekcji-akcji
- arkusz ogólnych w³asno¶ci oparty na introspekcji JavaBeans
- formaty plików XML oparte na standardzie PGML (wkrótce obs³uga SVG).

%package doc
Summary:	Javadoc for %{name}
Summary(pl):	Dokumentacja Javadoc dla %{name}
Group:		Documentation

%description doc
Javadoc for %{name}.

%description doc -l pl
Dokumentacja Javadoc dla %{name}.

%prep
%setup -q -c -T
mkdir src
cd src
unzip -q %{SOURCE0}
# remove binary files
find . -name "*.jar" -exec rm -f {} \;

%build
cd src
ant package

%install
rm -rf $RPM_BUILD_ROOT
install -D lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc src/COPYRIGHT src/INSTALL.txt src/readme.txt
%{_javadir}/*
